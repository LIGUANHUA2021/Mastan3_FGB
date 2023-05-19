###########################################################################################
#
# PyCMSect - Python-based Cross-platforms Section Analysis Software for Thin-walled Sections
#
# Developed by:
#   Siwei Liu   -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Wenlong Gao -   The Hong Kong Polytechnic University
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
def is_vector_between_two_vectors(t_YldSurf, dInsect_My_z):
    bool_value = 0
    ind_Loc = 666
    # dInsect_My_z[:, [0, 1]] = dInsect_My_z[:, [1, 0]]
    # t_YldSurf[:, [1, 2]] = t_YldSurf[:, [2, 1]]

    dInsect_My = dInsect_My_z[0]
    dInsect_Mz = dInsect_My_z[1]

    for jj in range(t_YldSurf.shape[0]):
        t_My1 = t_YldSurf[jj, 0]
        t_Mz1 = t_YldSurf[jj, 1]

        if jj == t_YldSurf.shape[0] - 1:
            t_My2 = t_YldSurf[0, 0]
            t_Mz2 = t_YldSurf[0, 1]
        else:
            t_My2 = t_YldSurf[jj + 1, 0]
            t_Mz2 = t_YldSurf[jj + 1, 1]

        td1 = (t_Mz1 * dInsect_My - t_My1 * dInsect_Mz) * (t_Mz1 * t_My2 - t_My1 * t_Mz2)
        td2 = (t_Mz2 * dInsect_My - t_My2 * dInsect_Mz) * (t_Mz2 * t_My1 - t_My2 * t_Mz1)

        if td1 >= 0 and td2 >= 0:
            ind_Loc = jj
            bool_value = 1
            break

    return bool_value, ind_Loc
