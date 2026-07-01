import sys
import os
from pathlib import Path
import shutil
import mimetypes


def create_qestion_folder(parent_folder_path:str,
                          main_asset_path:str,
                          question:str,
                          a_list:list,
                          a_correct:int,
                          loop:bool|int):

    if type(loop) == int:
        q_num = loop
        print(q_num)
        q_path = os.path.join(parent_folder_path,f"processed\\Question_{q_num}")
        os.makedirs(q_path,exist_ok=True)


        mimetypes.init()
        mime_start = mimetypes.guess_type(main_asset_path)[0]

        if mime_start != None:
            main_asset_type = mime_start.split('/')[0]
            print(main_asset_type)
            if main_asset_type not in ("video",'image'):
                raise ValueError("Main asset file type isin't expected video nor image")
        else:
            raise ValueError("Main asset file tyoe cannot be detected")
        

        d_to_save = {}
        d_to_save['question'] = question
        d_to_save["answers"] = a_list
        d_to_save['correct'] = a_correct
        d_to_save['type'] = main_asset_type


    return None


if __name__ =="__main__":
    path = Path().resolve()
    path  = path/"Data"
    print(os.path.exists(path))

    create_qestion_folder(path,r"C:\Users\kacpu\Programming projects\Teleturniej app\Data\raw\jamnik_6fc787d0-3c21-45ca-a74e-19610a2cc649.png","",[],1,1)