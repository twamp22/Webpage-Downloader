import os
import urllib.request
import urllib.error

class WebpageDownloader:
    def __init__(self, url):
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        self.url = url
        self.filename = self.generate_filename()

    def generate_filename(self):
        return self.url.replace('http://', '').replace('https://', '').replace('.', '_').replace('/', '_').replace('\\', '_') + '.html'

    def download(self):
        try:
            response = urllib.request.urlopen(self.url)
            web_content = response.read().decode('utf-8')
            
            os.makedirs('downloaded', exist_ok=True)
            full_path = os.path.join('downloaded', self.filename)
            
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(web_content)
            
            print(f"Webpage downloaded successfully and saved to '{os.path.abspath(full_path)}'")
        except urllib.error.URLError as e:
            print(f"Error: {e}")

class UserInputHandler:
    @staticmethod
    def get_url():
        return input("Enter the web address (URL) to download: ")

if __name__ == "__main__":
    url = UserInputHandler.get_url()
    downloader = WebpageDownloader(url)
    downloader.download()