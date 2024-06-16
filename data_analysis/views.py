from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def handle_uploaded_file(f):
    with open('temp.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_missing_values(df, strategy):
    if strategy == 'remove':
        df = df.dropna()
    elif strategy == 'mean':
        df = df.fillna(df.mean())
    elif strategy == 'median':
        df = df.fillna(df.median())
    return df

def process_data(request, file_path, strategy):
    df = pd.read_csv(file_path)
    df = handle_missing_values(df, strategy)
    summary_stats = df.describe().to_html()
    first_rows = df.head().to_html()
    missing_values = df.isnull().sum().reset_index().to_html(header=["Column", "Missing Values"])

    # Ensure the media directory exists before saving histograms
    if not os.path.exists('media'):
        os.makedirs('media')

    # Plot histograms
    histograms = []
    for column in df.select_dtypes(include=[np.number]).columns:
        plt.figure()
        sns.histplot(df[column].dropna(), kde=False)
        plt.title(f'Histogram of {column}')
        histogram_path = os.path.join('media', f'{column}_hist.png')
        plt.savefig(histogram_path)
        histograms.append(f'{column}_hist.png')
        plt.close()

    context = {
        'summary_stats': summary_stats,
        'first_rows': first_rows,
        'missing_values': missing_values,
        'histograms': histograms
    }
    return render(request, 'data_analysis/results.html', context)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            strategy = form.cleaned_data['handling_choice']
            return process_data(request, 'temp.csv', strategy)
    else:
        form = UploadFileForm()
    return render(request, 'data_analysis/upload.html', {'form': form})
