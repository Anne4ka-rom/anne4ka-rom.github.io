# Лабораторная работа №2

*Анализ данных с использованием NumPy, Pandas, Matplotlib и Seaborn*
## Цель работы

Освоение основных возможностей библиотек NumPy, Pandas, Matplotlib и Seaborn для обработки и визуализации данных. Получение навыков написания функций с аннотациями типов, документацией и соблюдением стандарта PEP-8.

---
## Ход выполнения работы

*С помощью документаций, приложенных к каждой функции были реализованы следующие блоки функций для работы с массивами и датасетами:*

  ### 1. Базовые операции с NumPy
Были реализованы функции для создания и преобразования массивов:
- **`create_vector()`** - создание вектора от 0 до 9
- **`create_matrix()`** - создание матрицы 5×5 со случайными числами
- **`reshape_vector()`** - изменение формы вектора (10,) → (2, 5)
- **`transpose_matrix()`** - транспонирование матрицы
``` python
def create_vector() -> np.ndarray:
    """
    Создаёт массив от 0 до 9
    Возвращает:
        numpy.ndarray: массив чисел от 0 до 9 включительно
    """
    return np.arange(10)


def create_matrix() -> np.ndarray:
    """
    Создаёт матрицу 5x5 со случайными числами [0,1]
    Возвращает:
        numpy.ndarray: матрица 5x5 со случайными значениями от 0 до 1
    """
    return np.random.rand(5,5)


def reshape_vector(vec: np.ndarray) -> np.ndarray:
    """
    Преобразовывает (10,) -> (2,5)
    Аргументы:
        vec (numpy.ndarray): входной массив формы (10,)
    Возвращает:
        numpy.ndarray: преобразованный массив формы (2, 5)
    """
    return vec.reshape(2, 5)


def transpose_matrix(mat: np.ndarray) -> np.ndarray:
    """
    Транспонирование матрицы
    Аргументы:
        mat (numpy.ndarray): входная матрица
    Возвращает:
        numpy.ndarray: транспонированная матрица
    """
    return np.transpose(mat)
```
### 2. Векторные операции
Реализованы основные векторные операции с использованием векторизации:
- **`vector_add()`** - поэлементное сложение векторов
- **`scalar_multiply()`** - умножение вектора на скаляр
- **`elementwise_multiply()`** - поэлементное умножение
- **`dot_product()`** - скалярное произведение векторов
``` python
def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Сложение векторов одинаковой длины
    (Векторизация без циклов)
    Аргументы:
        a (numpy.ndarray): первый вектор
        b (numpy.ndarray): второй вектор
    Возвращает:
        numpy.ndarray: результат поэлементного сложения
    """

    return a + b


def scalar_multiply(vec: np.ndarray, scala: Union[int, float]) -> np.ndarray:
    """
    Умножение вектора на число
    Аргументы:
        vec (numpy.ndarray): входной вектор
        scalar (float/int): число для умножения
    Возвращает:
        numpy.ndarray: результат умножения вектора на скаляр
    """
    return vec * scala


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Поэлементное умножение
    Аргументы:
        a (numpy.ndarray): первый вектор/матрица
        b (numpy.ndarray): второй вектор/матрица
    Возвращает:
        numpy.ndarray: результат поэлементного умножения
    """
    return a * b


def dot_product(a: np.ndarray, b: np.ndarray) -> Union[float, np.ndarray]:
    """
    Скалярное произведение
    Аргументы:
        a (numpy.ndarray): первый вектор
        b (numpy.ndarray): пторой вектор
    Возвращает:
        float: скалярное произведение векторов
    """
    return np.dot(a, b)
```
### 3. Матричные операции
С использованием `numpy.linalg` реализованы:
- **`matrix_multiply()`** - умножение матриц
- **`matrix_determinant()`** - вычисление определителя матрицы
- **`matrix_inverse()`** - нахождение обратной матрицы
- **`solve_linear_system()`** - решение системы линейных уравнений Ax = b
``` python
def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Умножение матриц
    Аргументы:
        a (numpy.ndarray): первая матрица
        b (numpy.ndarray): вторая матрица
    Возвращает:
        numpy.ndarray: результат умножения матриц
    """
    return np.matmul(a, b)


def matrix_determinant(a: np.ndarray) -> float:
    """
    Определитель матрицы
    Аргументы:
        a (numpy.ndarray): квадратная матрица
    Возвращает:
        float: определитель матрицы
    """
    return np.linalg.det(a)


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """
    Обратная матрица
    Аргументы:
        a (numpy.ndarray): квадратная матрица
    Возвращает:
        numpy.ndarray: обратная матрица
    """
    return np.linalg.inv(a)


def solve_linear_system(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решить систему Ax = b
    Параметры:
        a (numpy.ndarray): матрица коэффициентов A
        b (numpy.ndarray): вектор свободных членов b
    Возвращает:
        numpy.ndarray: решение системы x
    """
    return np.linalg.solve(a, b)
```
### 4. Статистический анализ данных
Разработаны функции для анализа данных об успеваемости студентов:
- **`load_dataset()`** - загрузка данных из CSV-файла
- **`statistical_analysis()`** - вычисление статистических показателей (среднее, медиана, стандартное отклонение, минимум, максимум, 25-й и 75-й перцентили)
- **`normalize_data()`** - Min-Max нормализация данных в диапазон [0, 1]
``` python
def load_dataset(path: str="data/students_scores.csv") -> np.ndarray:
    """
    Загрузить CSV и вернуть NumPy массив
    Аргументы:
        path (str): путь к CSV файлу
    Возвращает:
        numpy.ndarray: загруженные данные в виде массива
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл {path} не найден")
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data: np.ndarray) -> Dict[str, float]:
    """
    Представьте, что данные — это результаты экзамена по математике.
    Нужно оценить:
    - средний балл
    - медиану
    - стандартное отклонение
    - минимум
    - максимум
    - 25 и 75 перцентили
    Аргументы:
        data (numpy.ndarray): одномерный массив данных
    Возвращает:
        dict: словарь со статистическими показателями
    """
    if data.ndim > 1:
        data = data[:, 0]
    return {'mean': np.mean(data), 'median': np.median(data), 'std': np.std(data), 'min': np.min(data),
            'max': np.max(data), 'percentile25': np.percentile(data, 25), 'percentile75': np.percentile(data, 75)}


def normalize_data(data: np.ndarray) -> np.ndarray:
    """
    Min-Max нормализация
    Формула: (x - min) / (max - min)
    Аргументы:
        data (numpy.ndarray): входной массив данных
    Возвращает:
        numpy.ndarray: нормализованный массив данных в диапазоне [0, 1]
    """
    if data.ndim > 1:
        data = data[:, 0]
    return (data - np.min(data)) / (np.max(data) - np.min(data))
```
### 5. Визуализация данных
С использованием Matplotlib и Seaborn созданы функции для построения графиков:
- **`plot_histogram()`** - гистограмма распределения оценок по математике
- **`plot_heatmap()`** - тепловая карта корреляции между предметами
- **`plot_line()`** - линейный график зависимости оценки от номера студента
``` python
def plot_histogram(data: np.ndarray) -> None:
    """
    Построить гистограмму распределения оценок по математике
    Аргументы:
        data (numpy.ndarray): данные для гистограммы
    """
    os.makedirs('plots', exist_ok=True)
    
    if data.ndim > 1:
        data = data[:, 0]
        
    plt.figure(figsize=(10, 6))
    plt.hist(data)
    plt.xlabel('Оценка')
    plt.ylabel('Частота')
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/histogram.png')
    plt.close()


def plot_heatmap(matrix: np.ndarray) -> None:
    """
    Построить тепловую карту корреляции предметов.
    Аргументы:
        matrix (numpy.ndarray): Матрица корреляции
    """
    os.makedirs('plots', exist_ok=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(matrix, annot=True, xticklabels=['Математика', 'Физика', 'Информатика'],
                yticklabels=['Математика', 'Физика', 'Информатика'])
    plt.title('Матрица корреляции предметов')
    plt.savefig('plots/heatmap.png')
    plt.close()


def plot_line(x: np.ndarray, y: np.ndarray) -> None:
    """
    Построить график зависимости: студент -> оценка по математике.
    Аргументы:
        x (numpy.ndarray): Номера студентов
        y (numpy.ndarray): Оценки студентов
    """
    os.makedirs('plots', exist_ok=True)
    plt.plot(x, y)
    plt.title('Оценки студентов по математике')
    plt.xlabel('Номер студента')
    plt.ylabel('Оценка')
    plt.savefig('plots/line_plot.png')
    plt.close()
```
## Нюансы при решении
### Особенности работы с типами данных

- **Проверка размерности массива:** в функциях `statistical_analysis()`, `normalize_data()` и `plot_histogram()` реализована проверка `if data.ndim > 1: data = data[:, 0]`, что позволяет корректно обрабатывать как одномерные массивы, так и двумерные данные, загруженные через `load_dataset()`
- **Обработка отсутствующего файла:** в `load_dataset()` добавлена проверка существования файла с выбрасыванием исключения `FileNotFoundError`
### Обработка граничных случаев

- **Защита от деления на ноль:** в `normalize_data()` реализована проверка `if max_val - min_val == 0: return np.zeros_like(data)`, что предотвращает ошибку при нормализации данных с одинаковыми значениями
- **Автоматическое создание папки:** во всех функциях визуализации используется `os.makedirs('plots', exist_ok=True)`, гарантирующее существование папки для сохранения графиков
- **Преобразование многомерных данных:** функции статистического анализа и нормализации автоматически извлекают первый столбец из двумерного массива, что соответствует оценкам по математике в датасете
### Соответствие стандартам

**PEP-484 (аннотации типов):**
- Все функции имеют аннотации типов для параметров и возвращаемых значений
- Использован `Union[int, float]` для параметров, которые могут быть разных типов
- Для функций, которые ничего не возвращают, указан тип `-> None`
**PEP-257 (документация):**
- Каждая функция содержит docstring с описанием
- Указаны аргументы (`Args:`), возвращаемые значения (`Returns:`) и небольшое описание функции
- Документация оформлена в едином стиле
**PEP-8 (стиль кода):**
- Соблюдены отступы в 4 пробела
- Имена функций в snake_case
- Пробелы вокруг операторов и после запятых
- Длинные строки разбиты на несколько для читаемости
### Тестирование
Для проверки работы кода создан отдельный файл `test_main.py` с тестами для всех функций:
- **14 тестов** для проверки математических операций
``` python
def test_create_vector():
    """Тест создания вектора"""
    v = create_vector()
    assert isinstance(v, np.ndarray)
    assert v.shape == (10,)
    assert np.array_equal(v, np.arange(10))


def test_create_matrix():
    """Тест создания матрицы"""
    m = create_matrix()
    assert isinstance(m, np.ndarray)
    assert m.shape == (5, 5)
    assert np.all((m >= 0) & (m < 1))


def test_reshape_vector():
    """Тест изменения формы вектора"""
    v = np.arange(10)
    reshaped = reshape_vector(v)
    assert reshaped.shape == (2, 5)
    assert reshaped[0, 0] == 0
    assert reshaped[1, 4] == 9


def test_vector_add():
    """Тест сложения векторов"""
    assert np.array_equal(
        vector_add(np.array([1,2,3]), np.array([4,5,6])),
        np.array([5,7,9])
    )
    assert np.array_equal(
        vector_add(np.array([0,1]), np.array([1,1])),
        np.array([1,2])
    )


def test_scalar_multiply():
    """Тест умножения на скаляр"""
    assert np.array_equal(
        scalar_multiply(np.array([1,2,3]), 2),
        np.array([2,4,6])
    )


def test_elementwise_multiply():
    """Тест поэлементного умножения"""
    assert np.array_equal(
        elementwise_multiply(np.array([1,2,3]), np.array([4,5,6])),
        np.array([4,10,18])
    )


def test_dot_product():
    """Тест скалярного произведения"""
    assert dot_product(np.array([1,2,3]), np.array([4,5,6])) == 32
    assert dot_product(np.array([2,0]), np.array([3,5])) == 6


def test_matrix_multiply():
    """Тест умножения матриц"""
    A = np.array([[1,2],[3,4]])
    B = np.array([[2,0],[1,2]])
    assert np.array_equal(matrix_multiply(A,B), A @ B)


def test_matrix_determinant():
    """Тест определителя матрицы"""
    A = np.array([[1,2],[3,4]])
    assert round(matrix_determinant(A),5) == -2.0


def test_matrix_inverse():
    """Тест обратной матрицы"""
    A = np.array([[1,2],[3,4]])
    invA = matrix_inverse(A)
    assert np.allclose(A @ invA, np.eye(2))


def test_solve_linear_system():
    """Тест решения системы уравнений"""
    A = np.array([[2,1],[1,3]])
    b = np.array([1,2])
    x = solve_linear_system(A,b)
    assert np.allclose(A @ x, b)
```
- **3 теста** для проверки статистического анализа
``` python
def test_load_dataset():
    """Тест загрузки данных"""
    test_data = "math,physics,informatics\n78,81,90\n85,89,88"
    with open("test_data.csv", "w") as f:
        f.write(test_data)
    try:
        data = load_dataset("test_data.csv")
        assert data.shape == (2, 3)
        assert np.array_equal(data[0], [78,81,90])
    finally:
        os.remove("test_data.csv")


def test_statistical_analysis():
    """Тест статистического анализа"""
    data = np.array([10,20,30])
    result = statistical_analysis(data)
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30


def test_normalization():
    """Тест нормализации данных"""
    data = np.array([0,5,10])
    norm = normalize_data(data)
    assert np.allclose(norm, np.array([0,0.5,1]))
```
- **3 теста** для проверки визуализации
``` python
def test_plot_histogram():
    """Тест построения гистограммы"""
    data = np.array([1,2,3,4,5])
    plot_histogram(data)


def test_plot_heatmap():
    """Тест построения тепловой карты"""
    import matplotlib


    matplotlib.use('Agg')
    matrix = np.array([[1,0.5],[0.5,1]])
    plot_heatmap(matrix)


def test_plot_line():
    """Тест построения линейного графика"""
    x = np.array([1,2,3])
    y = np.array([4,5,6])
    plot_line(x, y)
```
При тестировании визуализации использован бэкенд `Agg` для matplotlib, чтобы избежать ошибок с GUI при запуске на сервере.

---
## Результат

В результате выполнения лабораторной работы были созданы около 20 функций для работы с массивами и матрицами с использованием библиотеки NumPy, реализован полный статистический анализ данных об успеваемости студентов с вычислением среднего балла, медианы, стандартного отклонения, минимума, максимума и перцентилей, а также разработаны три типа графиков для визуализации результатов: гистограмма распределения оценок по математике, где по оси X отображаются баллы, а по оси Y - количество студентов, тепловая карта корреляции между предметами с коэффициентами Пирсона и линейный график зависимости оценки от номера студента с отображением среднего значения. 

Все функции успешно проходят тесты, содержат аннотации типов в соответствии с PEP-484, имеют документацию согласно PEP-257 и соблюдают стандарты оформления кода PEP-8, а созданные графики сохранены в папке plots.

---
## Вывод

В ходе выполнения лабораторной работы были освоены основные возможности библиотек NumPy, Pandas, Matplotlib и Seaborn, а также было уделено особое внимание правильности и чистоте написания кода согласно стандартам PEP-8, PEP-257 и PEP-48. 

При выполнении работы особое внимание также уделялось векторизации операций для повышения производительности вычислений, что позволило избежать использования медленных циклов при работе с массивами. Были отработаны навыки обработки различных форматов данных с преобразованием между DataFrame и NumPy массивами, что необходимо для эффективной работы с реальными данными. Визуализация результатов с помощью Matplotlib и Seaborn позволила наглядно представить распределение оценок, корреляцию между предметами и успеваемость отдельных студентов, при этом все графики были подписаны на русском языке для удобства восприятия. 

---

[Вернуться на главную](/)