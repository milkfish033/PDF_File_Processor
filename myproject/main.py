from flask import *
import os 
import pdf_reader

app = Flask(__name__) 
#specify file path here where the uploaded file will be stored
save_file = '********************'
app.config[save_file] = save_file

@app.route('/') 

def main(): 
	#whenever using render_template, you are supposed to creat a templates file and stroe the file
	#which will be used later in the template file
	return render_template("index.html") 

@app.route('/success', methods = ['POST'])

def success():

	if request.method == 'POST': 
		w = request.form['user_text']
		f = request.files['file'] 
		#['file']: This part of the code accesses a specific file from the uploaded files dictionary. 
		#In your case, it's accessing the file uploaded with the name "file." 
		#This corresponds to the name of the file input field in your HTML form (<input type="file" name="file" />).
		
		f.save(os.path.join(app.config[save_file], f.filename))
		filepath = save_file+"/"+f.filename
		
		result = pdf_reader.generate([filepath], w)
		return render_template("Acknowledgement.html", name = f.filename, r = result) 
		#variable  name is used later in the Acknowledgement.html# 


if __name__ == '__main__':  
	app.run()

