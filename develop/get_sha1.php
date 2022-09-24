<?php


$version = isset($argv)? $argv[1]: '6.11';

$file = '/mnt/user/jonathan/git/unRAID/plugins/unRAID-NerdPack/packages/6.11/utf8proc-2.7.0-x86_64-1.txz';

$sha=file_check_sha1($file,'904236d09f2f6912e2d7d44dfd23354ee9a411ee');



$array = array();

$files = glob("/mnt/user/jonathan/git/unRAID/plugins/unRAID-NerdPack/packages/$version/*.{txz,tgz}", GLOB_BRACE);
foreach($files as $txz){
    //echo $txz, "\n";
   

    $array[] = file_check_sha1($txz);
}







// Compare the github sha1 value of a file
function file_check_sha1($file) {
    global $version;

    $size = filesize($file);
    $contents = file_get_contents($file);

    // create a sha1 like github does
    $str = "blob ".$size."\0".$contents;
    $sha1_file = sha1($str);

    $detalle = array();

    #print('Downloading file_check_sha1 => size ['.$size.'] package...');
    #print('Downloading file_check_sha1 => sha1_file ['.$sha1_file.'] package...');
    #print('Downloading file_check_sha1 => sha1_file ['.sha1($contents).'] package...');

    //echo "$file => $sha1_file => $size \n";
    $detalle['name'] = basename($file);
    $detalle['path'] = "packages/$version/".basename($file);
    $detalle['sha'] = $sha1_file;
    $detalle['size'] = $size;
    $detalle['download_url'] = "https://raw.githubusercontent.com/jsavargas/unRAID-NerdPack/update/packages/$version/".basename($file);
    $detalle['type'] = 'file';

    //print_r($detalle);
    //print_r($detalle);
    
    return ($detalle);
}

echo json_encode($array,JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES );



?>
