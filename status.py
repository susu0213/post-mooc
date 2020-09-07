curl "http://mooc1.chaoxing.com/ananas/status/${1}?k=${2}&flag=normal&_dc=`date +%s`" \
  -H 'Connection: keep-alive' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Accept: */*' \
  -H 'Referer: http://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2020-0812-1144' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cookie: k8s-ed=f26efd1049244d0985fae02c136a68985637b0f0; jrose=706B316C8E753E769A798FA3C883497B.html-editor-a-636674712-m458v; k8s=270da8e519d98d2e94be43c08aa6a114a4014232; route=2fe558bdb0a1aea656e6ca70ad0cad20; jrose=04EE1775D396F3AB669EB38FB844B516.mooc-3237058091-76m2f; fanyamoocs=11401F839C536D9E; isfyportal=1; lv=0; fid=62991; _uid=144212682; uf=fbe48ba271b0dbbd299fecfdc2980b779c697b754ad467dba4fcfdf12581e8b8b3404048ef0f5ae4483c180e83996625428b5a98cdb27be888b83130e7eb47048d3d04eb12c717c548b0f229181cd078b027a337608be8d61801e71c757b87b82b4570abd030a000e7fafd565af53bf2; _d=1599480314955; UID=144212682; vc=8F4D95A859C0F2F954D36ADD7764F9DC; vc2=A87389BC2CB13725393C2EF79D37FD7E; vc3=CDTq0CLuyvotvHvnFsTd%2B1Dov2e1w4J4MLS7s07qPdKUzrSh9CIriAPOOPcuxgpS7zNMSMXOzI4cpEXjL%2FCbU9iUjlJFgI1D5klkqITj7IMCszKzobpXgvRZ4oROGwcys8TXjWZ1%2FatYKcyW%2B3Be%2FjN7aAZIDgWD%2B0NRHdwHElk%3D31e04ff3047ba500969d6a8335160500; xxtenc=cc1f6b6aa2da596db677c2801fda7796; DSSTASH_LOG=C_38-UN_59061-US_144212682-T_1599480314956; source=""; thirdRegist=0; schoolId=62991; videojs_id=9247827' \
  --compressed \
  --insecure
