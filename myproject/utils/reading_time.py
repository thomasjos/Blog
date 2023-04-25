def estimate_reading_time(word_count, words_per_minute=200):
    reading_time = word_count / words_per_minute
    return round(reading_time)
