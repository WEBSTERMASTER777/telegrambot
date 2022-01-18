import torch
from torchvision import transforms
from PIL import Image
from yaml import load
from yaml import FullLoader
from json import dump

def load_config(config_file):
    with open(config_file) as f:
        return load(f, Loader=FullLoader)


def load_image(infilename):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    img = Image.open(infilename)
    img = transform(img)
    img = img.reshape(1, 3, 256, 256)
    return img

def load_class_names(filename):
    with open(filename) as f:
        return f.read().splitlines()    

def get_predict(img_name, model, class_names, device):
    pred_list = []
    model.eval()
    img = load_image(img_name)
    pred_list = model(img).sort(descending=True)[1].tolist()
    return pred_list[0]


def show_predict_bot(predictions, topn, class_names):
    class_name = load_class_names(class_names)
    s = f'TOP {topn} Network prediction:\n'
    for top, pred in enumerate(predictions[:topn]):
        s+=(f'\t{top+1} {class_name[pred]} \n')
    return s

def predforbot(img):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    config = load_config('config/script_percep_param.yaml')
    model = torch.jit.load(config['model'])
    pred = get_predict(img,
                       model,
                       config['class_names'],
                       device)
    pred = show_predict_bot(pred, config['topn'], config['class_names'])                  
    print(pred)
    return pred
    


