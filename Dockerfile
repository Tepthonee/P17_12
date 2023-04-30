FROM Tepthonee/thetepthon:slim-buster

 #clonning repo 
 RUN git clone https://github.com/Tepthonee/thetepthon.git /root/tepthon
 #working directory 
 WORKDIR /root/tepthon
 RUN apk add --update --no-cache p7zip
 # Install requirements
 RUN pip3 install --no-cache-dir -r requirements.txt
 ENV PATH="/home/tepthon/bin:$PATH"
 CMD ["python3","-m","tepthon"]
