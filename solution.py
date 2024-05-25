import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest as ztest


chat_id = 748421383 # Ваш chat ID, не меняйте название переменной

def solution(data: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.04
    # Рассчитываем t-статистику и p-значение
    t_stat, p_value = ztest(data, value=500) # используем z test
    
    # Сравниваем p-значение с уровнем значимости
    if p_value < alpha:
        return True  # Отклоняем нулевую гипотезу
    else:
        return False  # Не отклоняем нулевую гипотезу
