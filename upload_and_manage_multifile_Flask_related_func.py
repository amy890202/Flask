#藍圖
report = Blueprint('reportcase', __name__, template_folder='../templates')

#創暫時資料夾(不會和其他使用者共用)
import tempfile
dirname = tempfile.mkdtemp()

#python 的secur_filename函式無法處理中文，因此要把套件內容拿來改成支援中文
from werkzeug._compat import  PY2 ,text_type
import re
_windows_device_files = ('CON', 'AUX', 'COM1', 'COM2', 'COM3', 'COM4', 'LPT1',
                         'LPT2', 'LPT3', 'PRN', 'NUL')
def secure_filename(filename):
    if isinstance(filename, text_type):
        from unicodedata import normalize
        filename = normalize('NFKD', filename).encode('utf-8', 'ignore')  # 转码
        if not PY2:
            filename = filename.decode('utf-8')  # 解码
    for sep in os.path.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, ' ')

   #\u4E00-\u9FBF中文
    _filename_ascii_add_strip_re = re.compile(r'[^A-Za-z0-9_\u4E00-\u9FBF.-]')
    filename = str(_filename_ascii_add_strip_re.sub('', '_'.join(filename.split()))).strip('._')
    
    if os.name == 'nt' and filename and \
       filename.split('.')[0].upper() in _windows_device_files:
        filename = '_' + filename

    return filename
