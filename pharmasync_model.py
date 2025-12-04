import pandas as pd
from sklearn.cluster import KMeans

def find_best_window(df):
    # take only successful attempts
    success_df = df[df['success'] == 1]

    n = len(success_df)

    if n == 0:
        return "No successful data available to learn from."
    if n == 1:
        # Only one time → recommend 1-hour window around it
        centroid = int(success_df['time_in_minutes'].iloc[0])
        return _format_window(centroid, confidence=100)
    
    X = success_df[['time_in_minutes']]

    # dynamic clusters based on sample size
    cluster_options = [1]  # always allowed

    if n >= 2:
        cluster_options.append(2)
    if n >= 3:
        cluster_options.append(3)

    best_cluster_strength = -1
    best_centroid = None

    # Try dynamic cluster sizes
    for k in cluster_options:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
        labels = kmeans.fit_predict(X)
        centroids = kmeans.cluster_centers_

        for cluster_id in range(k):
            cluster_points = X[labels == cluster_id]
            strength = len(cluster_points)

            if strength > best_cluster_strength:
                best_cluster_strength = strength
                best_centroid = int(centroids[cluster_id][0])

    # Calculate confidence score
    confidence = round((best_cluster_strength / n) * 100, 2)

    return _format_window(best_centroid, confidence)


def _format_window(centroid, confidence):
    """Helper to format the 1-hour time window."""
    start_hour = centroid // 60
    start_min = centroid % 60
    window_start = f"{start_hour:02}:{start_min:02}"

    end_total = (centroid + 60) % 1440
    end_hour = end_total // 60
    end_min = end_total % 60
    window_end = f"{end_hour:02}:{end_min:02}"

    return window_start, window_end, confidence