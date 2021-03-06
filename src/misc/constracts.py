EXAM_TYPE = {'PURE_TONE': 'PURE_TONE', 'DICHOTIC': 'DICHOTIC', 'SPEECH_NOISE': 'SPEECH_NOISE'}
ROLES = {'ADMIN': 'ADMIN', 'USER': 'USER'}

EXAM_STATUS = {'DONE': 'DONE', 'PENDING': 'PENDING'}

right_silence = [
    ['صد'], ['بیخ'], ['تاج'], ['رس'], ['فاش'], ['ﻧﺎز'], ['دیگ'], ['آب', 'اب'], ['عید'], ['راز'], ['غم'],
    ['ایل'], ['دل'], ['تیغ'], ['یک'], ['به'], ['رب'], ['من'], ['شن'], ['تر'], ['پر'], ['کوه'], ['نم'],
    ['سن'], ['هم']
]

left_silence = [
    ['زن'], ['گل'], ['عید'], ['مه'], ['نم'], ['ری', 'ري'], ['پر'], ['چک'], ['حج'], ['این'], ['آش'], ['سیر'],
    ['شب'], ['بت'], ['نخ'], ['ناف'], ['تن'], ['سال'], ['مد'], ['ضد'], ['نام'], ['مین'], ['بار'], ['رود'],
    ['تیز']
]

right_noise = [
    ['موم'], ['میز'], ['تب'], ['راز'], ['جان'], ['خط'], ['پف', 'پوف'], ['قد'], ['کی', 'کي'], ['گاز'], ['این'],
    ['صد'], ['ول'], ['تاب'], ['لب'], ['کش'], ['رس'], ['من'], ['آش'], ['ایل'], ['روب', 'رب'], ['سن'], ['هیچ'],
    ['عید'], ['ده']
]

left_noise = [
    ['شش'], ['پور', 'پر'], ['تک'], ['ضد'], ['چین'], ['بد'], ['سن'], ['نان'], ['پر'], ['کاخ'], ['عید'], ['ماه'],
    ['ته'], ['غاز'], ['گیج'], ['ریز'], ['غم'], ['ول'], ['مال'], ['مخ'], ['بس'], ['این'], ['تر', 'تور'], ['مین'],
    ['به']
]

right_dichotic_binary = [[2, 9], [3, 8], [5, 1], [5, 8], [2, 5], [10, 1], [6, 9], [9, 1], [5, 2], [7, 5], [8, 2],
                         [9, 2],
                         [9, 3], [3, 8], [8, 1], [8, 10], [5, 3], [1, 2], [7, 5], [5, 7], [6, 7], [10, 7], [6, 7],
                         [10, 6], [1, 3]]
left_dichotic_binary = [[10, 3], [10, 6], [10, 8], [6, 9], [1, 3], [5, 2], [3, 5], [8, 10], [7, 6], [10, 8], [7, 9],
                        [5, 10], [1, 10], [5, 2], [10, 7], [6, 2], [8, 7], [3, 7], [3, 9], [9, 3], [10, 2], [8, 6],
                        [5, 10], [3, 2], [10, 9]]

right_dichotic_ternary = [[1,
                           8, 6], [10, 7, 9], [8, 5, 7], [7, 9, 5], [2, 5, 3], [7, 5, 10], [1, 10, 8], [10, 1, 7],
                          [6, 5, 10], [10, 3, 8], [3, 2, 5], [3, 2, 1], [8, 6, 1], [8, 7, 2], [6, 8, 1], [1, 3, 10],
                          [2, 3, 1], [5, 1, 8], [2, 6, 5], [10, 1, 6], [3, 7, 9], [9, 8, 2], [7, 2, 5], [6, 5, 10],
                          [2, 8, 6]]

left_dichotic_ternary = [[2, 10, 7], [8, 3, 6], [10, 6, 9], [1, 3, 8], [6, 8, 7], [6, 9, 8], [6, 7, 5], [6, 8, 2],
                         [1, 3, 2], [5, 2, 7], [1, 9, 7], [7, 5, 9], [7, 5, 10], [3, 9, 1], [7, 2, 5], [5, 9, 6],
                         [5, 10, 8], [9, 7, 6], [1, 9, 3], [7, 9, 5], [10, 6, 8], [10, 3, 6], [8, 3, 9], [3, 1, 9],
                         [3, 5, 10]]
