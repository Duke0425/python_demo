import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.filechooser import FileChooser, FileSystemAbstract, FileChooserIconLayout
from kivy.uix.filechooser import FileChooserIconView
import os
import platform

virtual_files = {
    "C:": {
        "size": 150,
        "files": {
            "a": {
                "size": 20,
                "files": {
                    "a1": {
                        "size": 30
                    }
                }
            },
            "b": {
                "size": 100
            },
            "c": {
                "size": 50,
                "files": {
                    "c1": {
                        "size": 10
                    },
                    "c2": {
                        "size": 50,
                        "files": {
        
                        }
                    }
                }
            }
        }
    }
}

class FileSystemVirtual(FileSystemAbstract):
    def __init__(self, files):
        self.files = files
        self.current_path = None
    
    def _collapse(self, nameparts):
        while '.' in nameparts:
            nameparts.remove('.')
        
        while '' in nameparts:
            nameparts.remove('')
        
        while '..' in nameparts:
            i = nameparts.index('..')
            nameparts = nameparts[:i - 1] + nameparts[i + 1:]
        
        return nameparts
    
    def _getentry(self, name):
        parts = name.strip('/').split('/')
        parts = self._collapse(parts)
        target = {'files': self.files, 'size': 0}
        while parts:
            nextpart = parts[0]
            parts = parts[1:]
            target = target['files'][nextpart]
        return target
    
    def listdir(self, fn):
        if "\\" in fn:
            fn = fn.replace('\\', '/')

        self.current_path = fn
        target = self._getentry(fn)
        if not target['files']:
            updateContent = {"c21": {
                                "size": 10000
                            }}
            target['files'] = updateContent
        if fn.endswith('/'):
            return [fn + keys for keys in target['files'].keys()]
        else:
            return [fn + '/' + keys for keys in target['files'].keys()]
        # return target['files'].keys()
    
    def getsize(self, fn):
        if "\\" in fn:
            fn = fn.replace('\\', '/')
        target = self._getentry(fn)
        return target['size']
    
    def is_hidden(self, fn):
        return False
    
    def is_dir(self, fn):
        if "\\" in fn:
            fn = fn.replace('\\', '/')
        target = self._getentry(fn)
        return 'files' in target


class CusFileChooser(FileChooser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class TestApp(App):
    def build(self):
        fc = FileChooserIconView(file_system=FileSystemVirtual(virtual_files), rootpath='C:')
        # fc.add_widget(FileChooserIconLayout())
        return fc

if __name__ == '__main__':
    TestApp().run()