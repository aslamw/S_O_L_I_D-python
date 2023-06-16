
"""
Neste exemplo, a classe FileManager tem a responsabilidade única de 
lidar com a leitura e escrita de arquivos. 
Cada método tem uma única tarefa relacionada a essa responsabilidade.
"""

class FileManager:
    def read_file(self, file_path):
        with open(file_path, 'r') as arq:
            data = arq.read()
        
        return data

    def write_file(self, file_path, data):
        with open(file_path, 'a') as arq:
            arq.write(data)
        return True 

    def format_data(self, data):
        format_new = '-'.join(data)

        return format_new

    def save_data(self, file_path, data):
        formatted_data = self.format_data(data)
        self.write_file(file_path, formatted_data)