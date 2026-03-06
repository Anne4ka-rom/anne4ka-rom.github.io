import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union, Dict, Any


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


# ============================================================
# 2. ВЕКТОРНЫЕ ОПЕРАЦИИ
# ============================================================


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


# ============================================================
# 3. МАТРИЧНЫЕ ОПЕРАЦИИ
# ============================================================

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


# ============================================================
# 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ
# ============================================================

def load_dataset(path: str="data/students_scores.csv") -> np.ndarray:
    """
    Загрузить CSV и вернуть NumPy массив
    
    Аргументы:
        path (str): путь к CSV файлу
    
    Возвращает:
        numpy.ndarray: загруженные данные в виде массива
    """
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
    return (data - np.min(data)) / (np.max(data) - np.min(data))


# ============================================================
# 5. ВИЗУАЛИЗАЦИЯ
# ============================================================

def plot_histogram(data: np.ndarray) -> None:
    """
    Построить гистограмму распределения оценок по математике
    
    Аргументы:
        data (numpy.ndarray): данные для гистограммы
    """
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
    plt.plot(x, y)
    plt.title('Оценки студентов по математике')
    plt.xlabel('Номер студента')
    plt.ylabel('Оценка')
    plt.savefig('plots/line_plot.png')
    plt.close()

if __name__ == "__main__":
    print("Запустите pytest test.py -v для проверки лабораторной работы.")