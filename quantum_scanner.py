"""
Quantum Readiness Scanner
Alat untuk mengaudit kesiapan website terhadap ancaman quantum computing
Dikembangkan untuk Tugas Audit TI - 2025
"""

import ssl
import socket
import requests
from urllib.parse import urlparse
from datetime import datetime
import json
from typing import Dict, List, Tuple
import time

class QuantumReadinessScanner:
    """
    Scanner untuk mengevaluasi kesiapan website terhadap ancaman quantum computing
    """
    
    # Cipher suites yang dianggap quantum-safe (post-quantum cryptography)
    QUANTUM_SAFE_CIPHERS = [
        'TLS_AES_256_GCM_SHA384',
        'TLS_CHACHA20_POLY1305_SHA256',
        'TLS_AES_128_GCM_SHA256'
    ]
    
    # Cipher suites yang rentan terhadap quantum computing
    QUANTUM_VULNERABLE_CIPHERS = [
        'RSA',
        'DH',
        'ECDH',
        'ECDSA'
    ]
    
    # Protokol TLS yang aman
    SECURE_TLS_VERSIONS = ['TLSv1.3', 'TLSv1.2']
    
    def __init__(self):
        self.results = []
        self.scan_time = datetime.now()
        
    def check_url_accessibility(self, url: str, timeout: int = 10) -> Tuple[bool, str]:
        """
        Memeriksa apakah URL dapat diakses
        
        Args:
            url: URL website yang akan diperiksa
            timeout: Batas waktu koneksi dalam detik
            
        Returns:
            Tuple (status_aksesibilitas, pesan_error)
        """
        try:
            response = requests.get(url, timeout=timeout, allow_redirects=True, verify=True)
            return True, f"HTTP {response.status_code}"
        except requests.exceptions.SSLError as e:
            return False, f"SSL Error: {str(e)[:100]}"
        except requests.exceptions.Timeout:
            return False, "Timeout"
        except requests.exceptions.ConnectionError as e:
            return False, f"Connection Error: {str(e)[:100]}"
        except Exception as e:
            return False, f"Error: {str(e)[:100]}"
    
    def get_ssl_info(self, hostname: str, port: int = 443) -> Dict:
        """
        Mengambil informasi SSL/TLS dari website
        
        Args:
            hostname: Nama host website
            port: Port yang digunakan (default 443)
            
        Returns:
            Dictionary berisi informasi SSL/TLS
        """
        ssl_info = {
            'tls_version': None,
            'cipher_suite': None,
            'certificate_valid': False,
            'certificate_issuer': None,
            'certificate_expires': None,
            'key_size': None
        }
        
        try:
            context = ssl.create_default_context()
            
            with socket.create_connection((hostname, port), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    # Dapatkan informasi TLS
                    ssl_info['tls_version'] = ssock.version()
                    ssl_info['cipher_suite'] = ssock.cipher()[0] if ssock.cipher() else None
                    
                    # Dapatkan informasi sertifikat
                    cert = ssock.getpeercert()
                    if cert:
                        ssl_info['certificate_valid'] = True
                        ssl_info['certificate_issuer'] = dict(x[0] for x in cert.get('issuer', []))
                        ssl_info['certificate_expires'] = cert.get('notAfter')
                        
                        # Dapatkan ukuran key dari public key
                        pubkey = ssock.getpeercert(binary_form=True)
                        if pubkey:
                            import cryptography.x509
                            from cryptography.hazmat.backends import default_backend
                            cert_obj = cryptography.x509.load_der_x509_certificate(pubkey, default_backend())
                            ssl_info['key_size'] = cert_obj.public_key().key_size
                            
        except Exception as e:
            ssl_info['error'] = str(e)[:200]
            
        return ssl_info
    
    def evaluate_quantum_readiness(self, ssl_info: Dict) -> Dict:
        """
        Mengevaluasi kesiapan quantum berdasarkan informasi SSL
        
        Args:
            ssl_info: Dictionary informasi SSL/TLS
            
        Returns:
            Dictionary hasil evaluasi
        """
        score = 0
        max_score = 100
        findings = []
        
        # Evaluasi 1: Versi TLS (30 poin)
        if ssl_info.get('tls_version') == 'TLSv1.3':
            score += 30
            findings.append("✓ Menggunakan TLS 1.3 (standar terbaru)")
        elif ssl_info.get('tls_version') == 'TLSv1.2':
            score += 20
            findings.append("⚠ Menggunakan TLS 1.2 (disarankan upgrade ke TLS 1.3)")
        else:
            findings.append("✗ Menggunakan versi TLS yang sudah usang dan tidak aman")
        
        # Evaluasi 2: Cipher Suite (40 poin)
        cipher = ssl_info.get('cipher_suite', '')
        is_quantum_safe = False
        
        for safe_cipher in self.QUANTUM_SAFE_CIPHERS:
            if safe_cipher in cipher:
                score += 40
                is_quantum_safe = True
                findings.append(f"✓ Menggunakan cipher quantum-safe: {cipher}")
                break
        
        if not is_quantum_safe:
            for vuln_cipher in self.QUANTUM_VULNERABLE_CIPHERS:
                if vuln_cipher in cipher:
                    findings.append(f"✗ Menggunakan cipher yang rentan quantum: {cipher}")
                    break
            else:
                score += 15
                findings.append(f"⚠ Menggunakan cipher: {cipher} (perlu evaluasi lebih lanjut)")
        
        # Evaluasi 3: Ukuran Key (20 poin)
        key_size = ssl_info.get('key_size')
        if key_size:
            if key_size >= 3072:
                score += 20
                findings.append(f"✓ Ukuran key kuat: {key_size} bit")
            elif key_size >= 2048:
                score += 10
                findings.append(f"⚠ Ukuran key standar: {key_size} bit (disarankan 3072+ bit)")
            else:
                findings.append(f"✗ Ukuran key lemah: {key_size} bit")
        
        # Evaluasi 4: Validitas Sertifikat (10 poin)
        if ssl_info.get('certificate_valid'):
            score += 10
            findings.append("✓ Sertifikat SSL valid")
        else:
            findings.append("✗ Sertifikat SSL tidak valid atau tidak ditemukan")
        
        # Tentukan status kesiapan
        if score >= 80:
            status = "Quantum-Ready"
            recommendation = "Website sudah memiliki kesiapan baik terhadap ancaman quantum"
        elif score >= 50:
            status = "Partially Ready"
            recommendation = "Website perlu peningkatan untuk menghadapi ancaman quantum"
        else:
            status = "Not Ready"
            recommendation = "Website sangat rentan dan perlu upgrade segera"
        
        return {
            'score': score,
            'max_score': max_score,
            'percentage': round((score / max_score) * 100, 2),
            'status': status,
            'findings': findings,
            'recommendation': recommendation
        }
    
    def scan_website(self, url: str) -> Dict:
        """
        Melakukan scan lengkap terhadap satu website
        
        Args:
            url: URL website yang akan di-scan
            
        Returns:
            Dictionary hasil scan lengkap
        """
        print(f"Scanning: {url}")
        
        result = {
            'url': url,
            'scan_time': datetime.now().isoformat(),
            'accessible': False,
            'ssl_info': {},
            'quantum_readiness': {}
        }
        
        # Parse URL untuk mendapatkan hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc or parsed_url.path
        
        # Hapus port jika ada
        if ':' in hostname:
            hostname = hostname.split(':')[0]
        
        # Check accessibility
        accessible, message = self.check_url_accessibility(url)
        result['accessible'] = accessible
        result['accessibility_message'] = message
        
        if accessible:
            # Get SSL info
            ssl_info = self.get_ssl_info(hostname)
            result['ssl_info'] = ssl_info
            
            # Evaluate quantum readiness
            if not ssl_info.get('error'):
                quantum_eval = self.evaluate_quantum_readiness(ssl_info)
                result['quantum_readiness'] = quantum_eval
            else:
                result['quantum_readiness'] = {
                    'status': 'Error',
                    'score': 0,
                    'error': ssl_info.get('error')
                }
        else:
            result['quantum_readiness'] = {
                'status': 'Inaccessible',
                'score': 0,
                'message': message
            }
        
        return result
    
    def scan_multiple_websites(self, urls: List[str], delay: float = 0.5) -> List[Dict]:
        """
        Melakukan scan terhadap multiple websites
        
        Args:
            urls: List URL yang akan di-scan
            delay: Jeda waktu antar scan (detik)
            
        Returns:
            List hasil scan
        """
        results = []
        total = len(urls)
        
        for idx, url in enumerate(urls, 1):
            print(f"\n[{idx}/{total}] Scanning: {url}")
            
            try:
                result = self.scan_website(url)
                results.append(result)
                
                # Tampilkan ringkasan hasil
                if result.get('accessible'):
                    qr = result.get('quantum_readiness', {})
                    print(f"  Status: {qr.get('status', 'Unknown')} - Score: {qr.get('score', 0)}/100")
                else:
                    print(f"  Status: Not Accessible - {result.get('accessibility_message', '')}")
                    
            except Exception as e:
                print(f"  Error: {str(e)}")
                results.append({
                    'url': url,
                    'error': str(e),
                    'scan_time': datetime.now().isoformat()
                })
            
            # Delay untuk menghindari rate limiting
            if idx < total:
                time.sleep(delay)
        
        self.results = results
        return results
    
    def save_results(self, filename: str = 'scan_results.json'):
        """
        Menyimpan hasil scan ke file JSON
        
        Args:
            filename: Nama file output
        """
        output = {
            'scan_metadata': {
                'scan_time': self.scan_time.isoformat(),
                'total_scanned': len(self.results),
                'scanner_version': '1.0.0'
            },
            'results': self.results
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"\nHasil scan disimpan ke: {filename}")
    
    def generate_summary(self) -> Dict:
        """
        Menghasilkan ringkasan statistik dari hasil scan
        
        Returns:
            Dictionary berisi statistik ringkasan
        """
        if not self.results:
            return {}
        
        total = len(self.results)
        accessible = sum(1 for r in self.results if r.get('accessible'))
        
        # Hitung berdasarkan status
        quantum_ready = 0
        partially_ready = 0
        not_ready = 0
        error = 0
        
        total_score = 0
        scored_count = 0
        
        for result in self.results:
            qr = result.get('quantum_readiness', {})
            status = qr.get('status', 'Unknown')
            
            if status == 'Quantum-Ready':
                quantum_ready += 1
            elif status == 'Partially Ready':
                partially_ready += 1
            elif status == 'Not Ready':
                not_ready += 1
            else:
                error += 1
            
            score = qr.get('score', 0)
            if score > 0:
                total_score += score
                scored_count += 1
        
        avg_score = round(total_score / scored_count, 2) if scored_count > 0 else 0
        
        summary = {
            'total_websites': total,
            'accessible': accessible,
            'inaccessible': total - accessible,
            'quantum_ready': quantum_ready,
            'partially_ready': partially_ready,
            'not_ready': not_ready,
            'error': error,
            'average_score': avg_score,
            'accessibility_rate': round((accessible / total) * 100, 2) if total > 0 else 0,
            'readiness_rate': round((quantum_ready / accessible) * 100, 2) if accessible > 0 else 0
        }
        
        return summary


def main():
    """
    Fungsi utama untuk menjalankan scanner
    """
    print("=" * 70)
    print("QUANTUM READINESS SCANNER")
    print("Audit Kesiapan Website terhadap Ancaman Quantum Computing")
    print("=" * 70)
    
    # Baca daftar website dari file
    try:
        with open('website_list.txt', 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print("Error: File 'website_list.txt' tidak ditemukan!")
        return
    
    print(f"\nTotal website yang akan di-scan: {len(urls)}")
    print("\nMemulai scanning...\n")
    
    # Inisialisasi scanner
    scanner = QuantumReadinessScanner()
    
    # Lakukan scanning
    results = scanner.scan_multiple_websites(urls, delay=0.5)
    
    # Simpan hasil
    scanner.save_results('scan_results.json')
    
    # Tampilkan ringkasan
    print("\n" + "=" * 70)
    print("RINGKASAN HASIL SCAN")
    print("=" * 70)
    
    summary = scanner.generate_summary()
    
    print(f"\nTotal Website: {summary['total_websites']}")
    print(f"Dapat Diakses: {summary['accessible']} ({summary['accessibility_rate']}%)")
    print(f"Tidak Dapat Diakses: {summary['inaccessible']}")
    
    print(f"\nStatus Kesiapan Quantum:")
    print(f"  ✓ Quantum-Ready: {summary['quantum_ready']}")
    print(f"  ⚠ Partially Ready: {summary['partially_ready']}")
    print(f"  ✗ Not Ready: {summary['not_ready']}")
    print(f"  ⚠ Error/Unknown: {summary['error']}")
    
    print(f"\nRata-rata Score: {summary['average_score']}/100")
    print(f"Tingkat Kesiapan Quantum: {summary['readiness_rate']}%")
    
    print("\n" + "=" * 70)
    print("Scan selesai! Jalankan dashboard untuk visualisasi interaktif.")
    print("Perintah: streamlit run dashboard.py")
    print("=" * 70)


if __name__ == "__main__":
    main()
