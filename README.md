# proxy.util   
![AWS](https://img.shields.io/badge/AWS-Supported-yellow)
![Azure](https://img.shields.io/badge/Azure-Supported-blue)
![DigitalOcean](https://img.shields.io/badge/Digital%20Ocean-In%20Progress-red)
## Abstract

A proxy network auto-repair pipeline based on Aliyun.  

## Setup  

1. Sign-up Aliyun OSS / CMS-SiteMonitor / EventBridge / RAM / FC / ACR Services.  
2. Create CMS-SiteMonitor task on the proxy network.  
3. Build docker image with VPC info locally using Dockerfile, then upload the image to ACR registry.  
4. Create FC with a CMS-SiteMonitor event trigger, executing user-defined initial instruction with docker images.  

## Flowchart  
TO DO
