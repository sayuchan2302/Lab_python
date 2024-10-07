def fill_missing_values(lst, method='mean', k=2):
    filled_lst = lst[:]  # Create a copy of the list
    missing_indices = [i for i, val in enumerate(lst) if val == -1]  # Find the indices of missing values (-1)
    non_missing_values = [val for val in lst if val != -1]  # List of values that are not missing

    # Calculate mean manually
    def calculate_mean(values):
        return sum(values) / len(values)

    # Calculate median manually
    def calculate_median(values):
        sorted_values = sorted(values)
        n = len(sorted_values)
        if n % 2 == 1:
            return sorted_values[n // 2]
        else:
            return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2

    # Filling based on the chosen method
    if method == 'mean':
        mean_value = calculate_mean(non_missing_values)  # Calculate the mean of non-missing values
        for idx in missing_indices:
            filled_lst[idx] = round(mean_value)  # Replace missing value with mean
    
    elif method == 'median':
        median_value = calculate_median(non_missing_values)  # Calculate the median of non-missing values
        for idx in missing_indices:
            filled_lst[idx] = round(median_value)  # Replace missing value with median

    elif method == 'kNN':
        # Replace missing values using the k-nearest neighbors method (default k=2)
        for idx in missing_indices:
            # Collect k nearest neighbors around the missing value
            neighbors = []
            if idx > 0:
                neighbors.append(lst[idx - 1])
            if idx < len(lst) - 1:
                neighbors.append(lst[idx + 1])
            
            # Compute the mean of the neighbors and replace the missing value
            knn_value = calculate_mean(neighbors)
            filled_lst[idx] = round(knn_value)

    return filled_lst

# Test the function with the default k=2
lst = [9, 10, 11, 12, -1, 14, 16, 19, 20, 24]
filled_mean = fill_missing_values(lst, 'mean')
filled_median = fill_missing_values(lst, 'median')
filled_knn = fill_missing_values(lst, 'kNN', k=2)

filled_mean, filled_median, filled_knn
print(filled_mean)
print(filled_median)   
print(filled_knn)
