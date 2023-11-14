var body = $response.body;
var obj = JSON.parse(body);

obj.limits = {
    "merge": {
      "mb": 4000,
      "files": 500
    },
    "split": {
      "mb": 4000,
      "files": 1
    },
    "compress": {
      "mb": 4000,
      "files": 10
    },
    "officepdf": {
      "mb": 4000,
      "files": 10
    },
    "wordpdf": {
      "mb": 4000,
      "files": 10
    },
    "powerpointpdf": {
      "mb": 4000,
      "files": 10
    },
    "excelpdf": {
      "mb": 4000,
      "files": 10
    },
    "pdfword": {
      "mb": 4000,
      "files": 10
    },
    "pdfpowerpoint": {
      "mb": 4000,
      "files": 10
    },
    "pdfexcel": {
      "mb": 4000,
      "files": 10,
      "pages": 400
    },
    "pdfoffice": {
      "mb": 4000,
      "files": 10
    },
    "pdfjpg": {
      "mb": 4000,
      "files": 10
    },
    "imagepdf": {
      "mb": 4000,
      "files": 80
    },
    "pagenumber": {
      "mb": 4000,
      "files": 10
    },
    "watermark": {
      "mb": 4000,
      "files": 10
    },
    "rotate": {
      "mb": 4000,
      "files": 80
    },
    "unlock": {
      "mb": 4000,
      "files": 10
    },
    "protect": {
      "mb": 4000,
      "files": 80
    },
    "pdfa": {
      "mb": 4000,
      "files": 10
    },
    "repair": {
      "mb": 4000,
      "files": 10
    },
    "organize": {
      "mb": 4000,
      "files": 20
    },
    "resizeimage": {
      "mb": 4000,
      "files": 120
    },
    "compressimage": {
      "mb": 4000,
      "files": 120
    },
    "cropimage": {
      "mb": 4000,
      "files": 1
    },
    "converttojpg": {
      "mb": 4000,
      "files": 120
    },
    "convertfromjpg": {
      "mb": 4000,
      "files": 120
    },
    "rotateimage": {
      "mb": 4000,
      "files": 120
    },
    "watermarkimage": {
      "mb": 4000,
      "files": 120
    },
    "memeimage": {
      "mb": 4000,
      "files": 1
    },
    "editimage": {
      "mb": 50,
      "files": 1
    },
    "editpdf": {
      "mb": 100,
      "files": 1
    },
    "sign": {
      "mb": 50,
      "files": 5
    }
  },
  
  obj.premium = true,
  obj.sus_rbt = true,



body = JSON.stringify(obj);
$done({body});
