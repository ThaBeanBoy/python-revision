class Size:
    """
    Contains height and width properties
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def equal(self, other):
        """
        Checks if the sizes of this and other are the same
        :param other: other Size object to be compared with
        :return: Boolean, whether the sizes are the same
        """
        other_size = matrix_size(other)
        return (self.height == other_size.height) and (self.width == other_size.width)


def matrix_size(matrix):
    """
    Takes in a 2d list and calculates the size of a matrix.
    NB: Throws ValueError exception if all the rows are not the same length
    :param matrix: the matrix
    :return: `Size`, the size of the given matrix
    """
    height = len(matrix)

    width = len(matrix[0])
    if not all(len(row) == width for row in matrix):
        raise ValueError("Not all rows in matrix are the same size")

    return Size(height, width)


def add_matrices(matrix1, matrix2):
    """
    Adds 2 matrices together
    :param matrix1: First matrix
    :param matrix2: Second matrix
    :return: final value of the addition
    """
    m1_size = matrix_size(matrix1)

    if m1_size.equal(matrix2):
        answer = []
        for y_index in range(m1_size.height):

            row_answer = []

            for x_index in range(m1_size.width):
                m1_cell_value = matrix1[y_index][x_index]
                m2_cell_value = matrix2[y_index][x_index]
                cell_answer = m1_cell_value + m2_cell_value
                row_answer.append(cell_answer)

            answer.append(row_answer)

        return answer

    else:
        raise ValueError('Matrices are not the same size')
