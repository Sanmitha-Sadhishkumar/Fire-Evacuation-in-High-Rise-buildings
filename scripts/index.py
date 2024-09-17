from flask import Flask, render_template, request, redirect, url_for
import subprocess, os, requests
from web_scraping import *
from rename import *
from yolov8_script import *
from decision_tree import *
from random_forest import *
import sys
import shutil
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
from yolov8_script import *

paths = [r'..\yolov5\runs\detect', r'..\yolov5\runs\val', r'..\yolov5\runs\train', '/uploads']
for i in paths:
  if os.path.exists(i):
    if os.path.isfile(i):
      os.remove(i)
    elif os.path.isdir(i):
      shutil.rmtree(i)

for i in os.listdir('../static'):
   if i not in ['show', 'model.glb']:
      if os.path.exists(f'../static{i}'):
        os.remove(f'../static{i}')

app = Flask(__name__, template_folder='../templates', static_url_path='', static_folder='../static',)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/lit_sur', methods=['GET', 'POST'])
def lit_sur():
    return render_template("lit_sur.html")

@app.route('/glb', methods=['GET', 'POST'])
def glb():
    return render_template("glb_viewer.html")

@app.route('/web_scraping', methods=['GET', 'POST'])
def web_scraping():
    return render_template("web_scraping.html", loader=True)

@app.route('/adult_children_elderly', methods=['GET', 'POST'])
def adult_children_elderly():
    return render_template("adult_vs_children.html", loader=True)

@app.route('/hbyolo', methods=['GET', 'POST'])
def hbyolo():
    return render_template("human_behaviour yolo.html", loader=True)

@app.route('/hbyolov8', methods=['GET', 'POST'])
def hbyolov8():
    return render_template("human_behaviour yolov8.html", loader=True)

@app.route('/lpg_scrap', methods=['GET', 'POST'])
def lpg_scrap():
    #result = web_scrap(lpg, '/content/lpg_dataset')
    result = web_scrap(['https://www.freepik.com/free-photos-vectors/lpg-gas'],'./lpg_dataset')
    print(result)
    imgs = os.listdir('./lpg_dataset')[:4]
    print(imgs)
    for i in imgs:
      print(os.getcwd())
      shutil.copy(f'./lpg_dataset/{i}', "../static/")
    #rename_files_in_folder(folder_path = r'/content/static/', file_extension='.jpg')
    return render_template("web_scraping.html", urls=lpg, result=result, sample_imgs = True, imgs=imgs, loader=True)

@app.route('/flammable_scrap', methods=['GET', 'POST'])
def flammable_scrap():
    #result = web_scrap(lpg, '/content/lpg_dataset')
    result = web_scrap(['https://www.freepik.com/free-photos-vectors/lpg-gas'],'./lpg_dataset')
    imgs = os.listdir('./lpg_dataset')[:4]
    for i in imgs:
      shutil.copy(f'./lpg_dataset/{i}', "../static/")
    #rename_files_in_folder(folder_path = r'/content/static/', file_extension='.jpg')
    return render_template("web_scraping.html", urls=lpg, result=result, sample_imgs = True, imgs=imgs, loader=True)

@app.route('/child_scrap', methods=['GET', 'POST'])
def child_scrap():
    #result = web_scrap(child_urls, '/content/child')
    result = web_scrap(['https://www.istockphoto.com/search/2/image-film?phrase=children&page=2'],'./child')
    imgs = os.listdir('./child')[:4]
    for i in imgs:
      shutil.copy(f'./child/{i}', "../static/")
    #rename_files_in_folder(folder_path = r'/content/static/', file_extension='.jpg')
    return render_template("web_scraping.html", urls=child_urls, result=result, sample_imgs = True, imgs=imgs, loader=True)

@app.route('/elderly_scrap', methods=['GET', 'POST'])
def elderly_scrap():
    #result = web_scrap(elderly_urls, '/content/elderly')
    result = web_scrap(['https://www.gettyimages.in/search/2/image-film?phrase=indian%20elderly&sort=mostpopular&page=2'],'./elderly')
    imgs = os.listdir('./elderly')[:4]
    for i in imgs:
      shutil.copy(f'./elderly/{i}', "../static/")
    #rename_files_in_folder(folder_path = r'/content/static/', file_extension='.jpg')
    return render_template("web_scraping.html", urls=elderly_urls, result=result, sample_imgs = True, imgs=imgs, loader=True)

@app.route('/hytrain', methods=['POST'])
def hytrain():
    res=''
    imgs=[]
    if 'runs' in os.listdir("../yolov5"):
      if 'train' in os.listdir("../yolov5/runs/"):
        prev_exp = os.listdir("../yolov5/runs/train")
      else:
        prev_exp=[]
    else:
      prev_exp=[]
    epochs = request.form['epochs-input']
    print(epochs)
    train_args = [
    "python", '../yolov5/train.py', '--img', '640', '--batch', '2', '--epochs', str(epochs),
    '--data', '../human_data.yaml', '--weights', 'yolov5s.pt', '--cache'
    ]
    print("Training started")
    try:
      result = subprocess.run(train_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
      print(result.stdout.decode('utf-8'))
      res = result.stdout.decode('utf-8')
      print(res)
      pres_exp = os.listdir("../yolov5/runs/train")
      exp = list(set(pres_exp)-set(prev_exp))[0]
      print(exp)
      res+=f'<br/><br/>Result stored in the folder : ../yolov5/runs/train/{exp}'
      print('Testing ended successfully')
      imgs = os.listdir(f'../yolov5/runs/train/{exp}')
      for i in imgs:
        shutil.copy(f'../yolov5/runs/train/{exp}/{i}', "../static/")
      print('Training ended successfully')
    except subprocess.CalledProcessError as e:
      print(f"Error during training: {e.stderr.decode('utf-8')}")
    return render_template("human_behaviour yolo.html", loader=True, result =res.replace('\n', '<br/>'), sample_imgs = True, imgs=imgs)

@app.route('/hytest', methods=['POST'])
def hytest():
    res=''
    imgs=[]
    if 'runs' in os.listdir("../yolov5"):
      if 'val' in os.listdir("../yolov5/runs/"):
        prev_exp = os.listdir("../yolov5/runs/val")
      else:
        prev_exp=[]
    else:
      prev_exp=[]
    train_args = [
    "python", "../yolov5/val.py", '--weights', '../models/yolov5_30.pt', '--data',
    '../human_data.yaml', '--task', 'val'
    ]
    print("Testing started")
    try:
      result = subprocess.run(train_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
      res = result.stdout.decode('utf-8')
      print(res)
      pres_exp = os.listdir("../yolov5/runs/val")
      exp = list(set(pres_exp)-set(prev_exp))[0]
      print(exp)
      res+=f'<br/><br/>Result stored in the folder : ../yolov5/runs/val/{exp}'
      print('Testing ended successfully')
      imgs = os.listdir(f'../yolov5/runs/val/{exp}')
      for i in imgs:
        shutil.copy(f'../yolov5/runs/val/{exp}/{i}', "../static/")
    except subprocess.CalledProcessError as e:
      print(f"Error during training: {e.stderr.decode('utf-8')}")
    return render_template("human_behaviour yolo.html", loader=True, result =res.replace('\n', '<br/>'), sample_imgs = True, imgs=imgs)

@app.route('/hydata', methods=['POST'])
def hydata():
  train = os.listdir("../datasets/human_dataset/images/train")
  val = os.listdir("../datasets/human_dataset/images/val")
  timgs = train[:4]
  for i in timgs:
      shutil.copy(f'../datasets/human_dataset/images/train/{i}', "../static/")
  vimgs = val[-4:]
  for i in vimgs:
      shutil.copy(f'../datasets/human_dataset/images/val/{i}', "../static/")
  imgs = timgs + vimgs
  result = f'''Train images {len(train)}<br/><br>
  Val images : {len(val)}<br/><br>
  Dataset source : Kaggle<br/>
  <a href="https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset">Human Detection Dataset</a><br>
  <a href="https://www.kaggle.com/datasets/jonathannield/cctv-human-pose-estimation-dataset?resource=download">CCTV Human Pose Estimation Dataset</a>'''
  return render_template("human_behaviour yolo.html", loader=True, result = result, sample_imgs = True, imgs = imgs)

@app.route('/hypredict', methods=['GET','POST'])
def hypredict():
    result=''
    if 'runs' in os.listdir("../yolov5"):
      if 'detect' in os.listdir("../yolov5/runs/"):
        prev_exp = os.listdir("../yolov5/runs/detect")
      else:
        prev_exp=[]
    else:
      prev_exp=[]
    tf = request.files['test-file']
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(uploads_dir):
      os.makedirs(uploads_dir)
    file_path = os.path.join(uploads_dir, tf.filename)
    tf.save(file_path)
    print(tf)
    detect_args = ["python", "../yolov5/detect.py", "--weights", "../models/yolov5_30.pt", "--img", "640", "--conf", "0.25", "--source", file_path, "--save-crop"]
    print("Prediction started")
    try:
      result = subprocess.run(detect_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)
      print(result.stdout.decode('utf-8'))
      res = result.stdout.decode('utf-8')
      print('Prediction ended successfully')
      pres_exp = os.listdir("../yolov5/runs/detect")
      exp = list(set(pres_exp)-set(prev_exp))[0]
      print(exp)
      res+=f'<br/><br/>Result stored in the folder : ../yolov5/runs/detect/{exp}'
      imgs = [i for i in os.listdir(f'../yolov5/runs/detect/{exp}') if i!='crops']
      print(imgs)
      for i in imgs:
          print(i)
          shutil.copy(f'../yolov5/runs/detect/{exp}/{i}', f"../static/")
    except subprocess.CalledProcessError as e:
      print(f"Error during Prediction: {e.stderr.decode('utf-8')}")
    return render_template("human_behaviour yolo.html", loader=True, result =res.replace('\n', '<br/>'), sample_imgs = True, imgs=imgs)

@app.route('/hyresults', methods=['GET', 'POST'])
def hyresults():
   imgs1 = [f'/yolo_result/epochs_10/'+i for i in os.listdir(f'../static/yolo_result/epochs_10') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs2 = [f'/yolo_result/epochs_20/'+i for i in os.listdir(f'../static/yolo_result/epochs_20') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs3 = [f'/yolo_result/epochs_30/'+i for i in os.listdir(f'../static/yolo_result/epochs_30') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs4 = [f'/yolo_result/epochs_40/'+i for i in os.listdir(f'../static/yolo_result/epochs_40') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs5 = [f'/yolo_result/epochs_50/'+i for i in os.listdir(f'../static/yolo_result/epochs_50') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs6 = [f'/yolo_result/epochs_60/'+i for i in os.listdir(f'../static/yolo_result/epochs_60') if (i.endswith('.jpg') or i.endswith('.png'))]
   return render_template("human_behaviour yolo.html", loader=True, res_table =True, res_imgs_bool=True, res_imgs1=imgs1, res_imgs2=imgs2, res_imgs3=imgs3, res_imgs4=imgs4, res_imgs5=imgs5, res_imgs6=imgs6)

@app.route('/hytrainv8', methods=['POST'])
def hytrainv8():
    res=''
    imgs=[]
    if 'runs' in os.listdir("../"):
      if 'detect' in os.listdir("./runs/"):
        prev_exp = os.listdir("../yolov5/runs/detect")
      else:
        prev_exp=[]
    else:
      prev_exp=[]
    epochs = request.form['epochs-input']
    print(epochs)
    res=yolov8_train(epochs)
    print("Training started")
    pres_exp = os.listdir("../runs/detect")
    exp = list(set(pres_exp)-set(prev_exp))[0]
    print(exp)
    res+=f'<br/><br/>Result stored in the folder : ./runs/detect/{exp}'
    print('Testing ended successfully')
    imgs = os.listdir(f'./runs/detect/{exp}')
    for i in imgs:
      shutil.copy(f'./runs/detect/{exp}/{i}', "../static/")
    print('Training ended successfully')
    return render_template("human_behaviour yolov8.html", loader=True, result =str(res).replace('\n', '<br>'), sample_imgs = True, imgs=imgs)

@app.route('/hytestv8', methods=['POST'])
def hytestv8():
    res=''
    imgs=[]
    if 'runs' in os.listdir("../"):
      if 'detect' in os.listdir("./runs/"):
        prev_exp = os.listdir("../yolov5/runs/detect")
      else:
        prev_exp=[]
    else:
      prev_exp=[]
    res=yolov8_val('../models/yolov8_30.pt')
    print("Testing started")
    pres_exp = os.listdir("../runs/detect")
    exp = list(set(pres_exp)-set(prev_exp))[0]
    print(exp)
    res+=f'<br/><br/>Result stored in the folder : ./runs/detect/{exp}'
    print('Testing ended successfully')
    imgs = os.listdir(f'./runs/detect/{exp}')
    for i in imgs:
      shutil.copy(f'./runs/detect/{exp}/{i}', "../static/")
    print('Testing ended successfully')
    return render_template("human_behaviour yolov8.html", loader=True, result =str(res).replace('\n', '<br>'), sample_imgs = True, imgs=imgs)

@app.route('/hypredictv8', methods=['GET','POST'])
def hypredictv8():
    res=''
    imgs=[]
    if 'runs' in os.listdir("../"):
      if 'detect' in os.listdir("./runs/"):
        prev_exp = os.listdir("./runs/detect")
      else:
        prev_exp=[]
    else:
      prev_exp=[]
    tf = request.files['test-file']
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(uploads_dir):
      os.makedirs(uploads_dir)
    file_path = os.path.join(uploads_dir, tf.filename)
    tf.save(file_path)
    print(tf)
    print("Prediction started")
    res = yolov8_detect('../models/yolov8_30.pt', file_path)
    print('Prediction ended successfully')
    pres_exp = os.listdir("./runs/detect")
    exp = list(set(pres_exp)-set(prev_exp))[0]
    print(exp)
    res+=f'<br/><br/>Result stored in the folder : ./runs/detect/{exp}'
    imgs = [i for i in os.listdir(f'./runs/detect/{exp}') if i!='crops']
    print(imgs)
    for i in imgs:
        print(i)
        shutil.copy(f'./runs/detect/{exp}/{i}', f"../static/")
    print(str(res))
    return render_template("human_behaviour yolov8.html", loader=True, result =str(res).replace('\n', '<br>'), sample_imgs = True, imgs=imgs)

@app.route('/hyresultsv8', methods=['GET', 'POST'])
def hyresultsv8():
   imgs1 = [f'/yolo_result/10 epochs/'+i for i in os.listdir(f'../static/yolo_result/10 epochs') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs2 = [f'/yolo_result/20 epochs/'+i for i in os.listdir(f'../static/yolo_result/20 epochs') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs3 = [f'/yolo_result/30 epochs/'+i for i in os.listdir(f'../static/yolo_result/30 epochs') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs4 = [f'/yolo_result/40 epochs/'+i for i in os.listdir(f'../static/yolo_result/40 epochs') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs5 = [f'/yolo_result/50 epochs/'+i for i in os.listdir(f'../static/yolo_result/50 epochs') if (i.endswith('.jpg') or i.endswith('.png'))]
   imgs6 = [f'/yolo_result/60 epochs/'+i for i in os.listdir(f'../static/yolo_result/60 epochs') if (i.endswith('.jpg') or i.endswith('.png'))]
   return render_template("human_behaviour yolov8.html", loader=True, res_table =True, res_imgs_bool=True, res_imgs1=imgs1, res_imgs2=imgs2, res_imgs3=imgs3, res_imgs4=imgs4, res_imgs5=imgs5, res_imgs6=imgs6)

@app.route('/acedata', methods=['GET', 'POST'])
def acedata():
    adult = os.listdir(r"..\datasets\adult_children_elderly\train\adults")
    children = os.listdir(r"..\datasets\adult_children_elderly\train\children")
    elderly = os.listdir(r"..\datasets\adult_children_elderly\train\elderly")
    aimgs = adult[:2]
    for i in aimgs:
      shutil.copy(f"../datasets/adult_children_elderly/train/adults/{i}", "../static/")
    cimgs = children[-2:]
    for i in cimgs:
      shutil.copy(f"../datasets/adult_children_elderly/train\children/{i}", "../static/")
    eimgs = elderly[20:40]
    for i in cimgs:
      shutil.copy(f"../datasets/adult_children_elderly/train\children/{i}", "../static/")
    imgs = aimgs + cimgs + eimgs
    result = f'''
    No. of Classes : 3 (Adult, Children, Elderly)<br><br>
    Train images:<br>
    Adult images :  {len(adult)}<br/>
    Children images : {len(children)}<br/>
    Elderly images : {len(elderly)}<br/><br>
    Dataset source : Kaggle and Image Scraping<br/>
    <a href="https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset">Human Detection Dataset</a><br>
    <a href="https://www.kaggle.com/datasets/jonathannield/cctv-human-pose-estimation-dataset?resource=download">CCTV Human Pose Estimation Dataset</a>'''
    return render_template("adult_vs_children.html", result=result)

@app.route('/dttrain', methods=['GET', 'POST'])
def dttrain():
    result = dt_train('./dt.pkl')
    return render_template("adult_vs_children.html", result=result.replace('\n', '<br>').replace(' ', '&nbsp;'))

@app.route('/dttest', methods=['GET', 'POST'])
def dttest():
    results = []
    res=''
    ov_res=0
    paths={'Adult':'../datasets/adult_children_elderly/test/adults', 'Children':'../datasets/adult_children_elderly/test/children', 'Elderly':'../datasets/adult_children_elderly/test/elderly', }
    for i in paths:
      result1=0
      ov_res += len(os.listdir(paths[i]))
      for filename in os.listdir(paths[i]):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(paths[i], filename)
            result = dec_dt(image_path)
            if result==i:
              results.append(result)
              result1+=1
      res+=f"Class : {i} Correct Predictions : {result1}<br>"
    res+=f'<br>Overall accuracy: {len(results)/ov_res}'
    return render_template("adult_vs_children.html", result=res)

@app.route('/dtpredict', methods=['GET', 'POST'])
def dtpredict():
    tf = request.files['test-file1']
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(uploads_dir):
      os.makedirs(uploads_dir)
    file_path = os.path.join(uploads_dir, tf.filename)
    tf.save(file_path)
    print(tf)
    result = dec_dt(file_path)
    return render_template("adult_vs_children.html", result=f"The predicted class for the image is: {result}")

@app.route('/rftrain', methods=['GET', 'POST'])
def rftrain():
    result = rf_train('./rf.pkl')
    return render_template("adult_vs_children.html", result=result.replace('\n', '<br>').replace(' ', '&nbsp;'))

@app.route('/rftest', methods=['GET', 'POST'])
def rftest():
    results = []
    res=''
    ov_res=0
    paths={'Adult':'../datasets/adult_children_elderly/test/adults', 'Children':'../datasets/adult_children_elderly/test/children', 'Elderly':'../datasets/adult_children_elderly/test/elderly', }
    for i in paths:
      result1=0
      ov_res += len(os.listdir(paths[i]))
      for filename in os.listdir(paths[i]):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(paths[i], filename)
            result = predict_image_class(image_path)
            if result==i:
              results.append(result)
              result1+=1
      res+=f"Class : {i} Correct Predictions : {result1}<br>"
    res+=f'<br>Overall accuracy: {len(results)/ov_res}'
    return render_template("adult_vs_children.html", result=res)

@app.route('/rfpredict', methods=['GET', 'POST'])
def rfpredict():
    tf = request.files['test-file2']
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(uploads_dir):
      os.makedirs(uploads_dir)
    file_path = os.path.join(uploads_dir, tf.filename)
    tf.save(file_path)
    print(tf)
    result = predict_image_class(file_path)
    return render_template("adult_vs_children.html", result=f"The predicted class for the image is: {result}")

if __name__ == "__main__":
    app.run(debug=True)