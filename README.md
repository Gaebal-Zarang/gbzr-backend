# Gaebal-Zarang-backend

## 📃 프로젝트 개요
- 사이드 프로젝트 및 스터디를 진행할 수 있도록, 협업자 매칭 서비스입니다.

## ⚙️ 개발 환경
- ![macosm1 badge](https://img.shields.io/badge/MacOS%20M1-000000.svg?style=flat&logo=macOS&logoColor=white)
- ![Visual Studio Code badge](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?style=flat&logo=Visual-Studio-Code&logoColor=white)
- ![github badge](https://img.shields.io/badge/GitHub-181717.svg?style=flat&logo=GitHub&logoColor=white)
- ![docker badge](https://img.shields.io/badge/Docker-2496ED.svg?style=flate&logo=Docker&logoColor=white)
- ![postman badge](https://img.shields.io/badge/postman-FF6C37?style=flat&logo=Postman&logoColor=white)
- ![swagger badge](https://img.shields.io/badge/Swagger-85EA2D.svg?style=flat&logo=Swagger&logoColor=black)

<br>

## 🛠 사용 기술
**Server**
- ![python badge](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=Python&logoColor=white)
- ![django badge](https://img.shields.io/badge/Django-4.1.7-%23092E20?&logo=Django&logoColor=white)

**Database**
- ![Postgres badge](https://img.shields.io/badge/postgres-14.5-%23316192.svg?style=flat&logo=postgresql&logoColor=white)

**Deploy (not yet)**
- ![aws ec2 badge](https://img.shields.io/badge/AWS-EC2-%23FF9900?&logo=Amazon%20EC2&logoColor=white)
- ![docker badge](https://img.shields.io/badge/Docker-20.10.17-%232496ED?&logo=Docker&logoColor=white)
- ![nginx badge](https://img.shields.io/badge/Nginx-1.23.0-%23009639?logo=NGINX&locoColor=white)
- ![Gunicorn badge](https://img.shields.io/badge/Gunicorn-499848.svg?style=flat&logo=Gunicorn&logoColor=white)


<br>

## 📙 API 명세서
### 👉 [📑 API Specification](https://sprinkle-piccolo-9fc.notion.site/API-Specification-gbzr-c287814a50c5452da4d9c2234c2adf75)
<!-- <img width="1176" alt="api 명세서" src=""> -->

<br>

## 📋 E-R Diagram
<img width="1000" alt="ERD" src="https://user-images.githubusercontent.com/51039577/216359977-d3818314-4d74-483f-a30e-7fce2f44a6f8.png">

❗️ User 모델은 장고의 기본 User 모델을 그대로 사용하지 않고 커스텀하였습니다.
❗️ created_at, updated_at 속성은 Common 모델을 상속받도록 구현했습니다.


<!-- ## ✅ Test Case
- Django에 내장된 테스트 모듈을 사용하여 유닛테스트를 진행하였습니다.
- 테스트 케이스를 작성함으로써, end-point의 수정이 있을 경우 정상 작동의 여부를 간편하게 확인할 수 있었습니다. -->
<!-- - 유저 생성 및 로그인, 로그아웃, 유저 조회 API와  상태 조회, 시작, 종료 API TESTCASE 수행 -->
<!-- <img width="1000" alt="Test Case" src=""> -->


<br>

## 🌍 배포 (not yet)
<!-- Docker, NginX, Gunicorn을 사용하여 AWS EC2 서버에 배포하였습니다.
➡️ [서비스 주소](13.124.201.55)

기본 URL은 404 페이지 입니다.

❗️ 현재 비용의 문제로 서버 접속은 불가능합니다. -->


<!-- ## 📂 Directory Structure
<img width="300" alt="Directory Structure" src="">

## 🕸 System Architecture
<img width="1000" alt="System Architecture" src=""> -->
---


<br>


<br>
<br>
<br>



<!-- ## Set-up requirement

- python version >= 3.10

## Setting steps

0. `pip install pyenv poetry`
1. `pyenv virtualenv (python-version) gbzr-backend` > create virtual-env
3. `pyenv local gbzr-backend` > set python-version in virtual-env

## Set-up steps

1. `pyenv shell gbzr-env`
2. `poetry shell` > activate virtualenv
3. `poetry update` or `poetry lock` > setting apply pyproject.toml
4. `python manage.py runserver` > start app
5. `python manage.py migrate` > for migration
6. `python manage.py createsuperuser` > create superuser(admin)

## Migration guide -->