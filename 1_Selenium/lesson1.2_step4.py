# Задание: интерпретатор Python
# Чтобы мы точно знали, что вы выполнили все инструкции и Python успешно установлен на ваш компьютер, запустите следующий код в интерпретаторе: 

import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))


# 723128532146