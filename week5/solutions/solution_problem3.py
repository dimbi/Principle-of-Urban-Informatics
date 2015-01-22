# Functions for students to implement.

naive = []
def buildNaive(points,n):
    # Removes previous data, if any.
    del naive[:]

    # Appends each new point to naive.
    for p in points:
        naive.append(p)

    return None

onedim = []
def buildOneDim(points,n):
    # Removes previous 1D partitions, if any.
    del onedim[:]

    # Creates n partitions (each partition is a 1D list of points).
    for i in range(n):
        onedim.append([])

    # Inserts points to corresponding partition.
    for p in points:
        # x, y coordinates
        x = p[0]
        y = p[1]

        # Computes partition index for this point.
        index_x = int(x * n)

        # Stores into partition.
        onedim[index_x].append(p)

    return None

twodim = []
def buildTwoDim(points,n):
    # Removes previous 2D partitions, if any.
    del twodim[:]

    # Creates n*n cells (each cell is a 1D list of points).
    for i in range(n):
        # For column i, creates list for rows.
        twodim.append([])

        for j in range(n):
            # For row j, creates list for points (a cell).
            twodim[i].append([])

    for p in points:
        # x, y coordinates
        x = p[0]
        y = p[1]

        # Computes partition index for this point (x direction).
        index_x = int(x * n)
        # Computes partition index for this point (y direction).
        index_y = int(y * n)

        # Stores into partition.
        twodim[index_x][index_y].append(p)

    return None


def queryNaive(x0, y0, x1, y1):
    count = 0

    # For each point, tests whether it is inside the query rectangle.
    for p in naive:
        x = p[0]
        y = p[1]

        # If point in rectangle, adds to count.
        if x >= x0 and y >= y0 and x <= x1 and y <= y1:
            count += 1

    return count

def queryOneDim(x0, y0, x1, y1):
    count = 0

    # Computes the indices of cells that need to be tested.
    n = len(onedim)

    # Cells between [index0, index1] (inclusive interval).
    index0 = int(x0 * n)
    index1 = int(x1 * n)

    for cell in onedim[index0:index1+1]:
        # For each point in cell, tests whether it is in the rectangle query.
        for p in cell:
            x = p[0]
            y = p[1]

            # If point in rectangle, adds to count.
            if x >= x0 and y >= y0 and x <= x1 and y <= y1:
                count += 1

    return count

def queryTwoDim(x0, y0, x1, y1):
    count = 0
    n = len(twodim)

    # Columns between [index_x0, index_x1] (inclusive interval).
    index_x0 = int(x0 * n)
    index_x1 = int(x1 * n)

    # Rows between [index_y0, index_y1] (inclusive interval).
    index_y0 = int(y0 * n)
    index_y1 = int(y1 * n)

    # For each column:
    for cellx in twodim[index_x0:index_x1+1]:
        # For each row:
        for celly in cellx[index_y0:index_y1+1]:
            # For each point in the cell:
            for p in celly:
                x = p[0]
                y = p[1]

                # If point in rectangle, adds to count.
                if x >= x0 and y >= y0 and x <= x1 and y <= y1:
                    count += 1

    return count
