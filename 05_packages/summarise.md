## Packages

#### import 'package'

    from A import B

1. B에 쓰여진 그대로 호출 가능하다.
2. package를 import할 때, __init__.py에 정의된 것 혹은 module만 참조한다.
3. A.B.C 와 같은 도트 연산자를 쓸때, 마지막 C에는 module 혹은 package만 가능하다.

#### __init__.py  

* __init__.py : package내의 directory가 package의 일부임을 알려주는 역할을 한다.
* __init__.py가 없으면 package로 인식하지 않는다.
* __all__ : module의 이름으로 이루어진 list로 /* 를 이용하여 import 할때, __all__ 을 참조하여 import 한다.
