# LaTeX2img
Not all the markdown render support LaTex function, so it will be annoyed when publishing your articles on
this website if there exists LaTex function. So I wrote this project to transfer LaTex function to image tag
automatically.

# How to use
first, clone this repository. Python3.X environment is needed.
```
git clone https://github.com/IamBusy/LaTeX2img.git
cd LaTeX2img
pip install -r requirements.txt
```

Then configure the storage in file `config.toml`
> Only [qiniu](https://www.qiniu.com) is supported now. Contribution of more drivers
is appreciated

```toml
access_key="your-access-key"
secret_key="your-secret-key"
bucket="your-bucket"
domain="your-domain"
prefix="prefix is optional"
```

Now enjoy it!
```
python main.py -i /the/path/or/file/of/*.mds -o /where/to/store/the/result
```