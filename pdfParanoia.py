#! python3

#PDF Paranoia
#encrypts all PDF's in a given folder

import shutil, os, docx, PyPDF2, send2trash

valid_path = False
while valid_path == False:
	#ask for folder name
	print('The current working directory is ' + os.getcwd())
	folder_to_encrypt = str(input('\nplease enter the absolute or relative path of the folder containing the PDFs you wish to encrypt.\n'))
	#check to make sure that is a valid path
	if os.path.exists(folder_to_encrypt):
		valid_path = True

#change current working directory to the folder containing files to be encrypted
os.chdir(folder_to_encrypt)

#checks to make sure there is not already a folder in the current directory called 'encrypted'
if not os.path.exists('.//encrypted'):
	#makes a folder to copy the encrypted files to inside the current directory (mostly helps with testing)
	os.makedirs('.//encrypted')


#find all files in that folder and subfolders
for folder_name, subfolders, filenames in os.walk(str(folder_to_encrypt)):
		for filename in filenames:
			

			#get a lot of 'EOF marker not found' errors wihtout this try-except
			try:
				#encrypt those files
				unencrypted_file = open(filename, 'rb')
				pdf_reader = PyPDF2.PdfFileReader(unencrypted_file)
				print('attempting to encrypt ' + filename)
				pdf_writer = PyPDF2.PdfFileWriter()

				for pageNum in range (pdf_reader.numPages):
					pdf_writer.addPage(pdf_reader.getPage(pageNum))
				pdf_writer.encrypt('daniel')
				#append '_encrypted' to the file name
				encrypted_file = open('encrypted//encrypted %s' % filename, 'wb')
				pdf_writer.write(encrypted_file)
				encrypted_file.close()
				#check that those files are encrypted
				if PyPDF2.PdfFileReader(open('encrypted//encrypted %s' %filename,'rb')).isEncrypted:
					print('%s has been encrypted succesfully' % filename)
					#delete those files
					#----------send2trash may be broken------------------
					#sends files to recycling bin, but does not remove them from the folder
					#send2trash.send2trash(str(filename))
					#print('WARNING!!! The unencrypted files are in the trash.')
				else:
					print('Sorry, human. I couldn\'t encrypt %s. The original will be retained')
				
			except:
				print('Sorry, human. I cannot open %s.' % filename)

				
			





