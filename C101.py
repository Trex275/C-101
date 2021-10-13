#Upload files to dropbox
import dropbox

class Transferdata: 
    def __init__(self, acess_token):
        self.acesstoken = acess_token
    def upload_file (self, file_from, file_to):
        """Upload a file to Dropbox using APIv2"""
        dbx = dropbox.Dropbox(self.acesstoken)
        with open (file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main(): 
    acess_token = 'sl.A6QMmkz7WVncBn5ZL-8Ls0CeCzmcUdBLfoYsWMHuwnis1zH2TxjnRqGRMF05OPZ32ttowfCmmM8ptAF1i92RABazqI9jwcl475aTLApOPIiFPDRKFYYBemkBoQ2oPea60hdB2mz3QXrK'
    transferdata = Transferdata(acess_token)

    file_from = input('Enter filepath of file you want to backup here:')
    file_to = input("Enter full path to upload to dropbox")

    transferdata.upload_file(file_from, file_to)
if __name__ == '__main__':
    main()