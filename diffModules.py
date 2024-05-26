import difflib

def compare_files(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        diff = difflib.unified_diff(
            f1.readlines(),
            f2.readlines(),
            fromfile=file1,
            tofile=file2,
        )
    return list(diff)

def write_diff(diff, file1, file2, diff_file):
    with open(diff_file, 'a') as f:
        f.write(f"----Diferencias entre {file1} y {file2}----\n")
        for line in diff:
            f.write(line)
        f.write("\n")
        
# Hardcodea los paths de los archivos
file1 = '/home/joaquin/Facu/TP4_SISTCOMP/TP4-Sistcomp/TP4-SistComp/loaded_modules_joaco.txt'
file2 = '/home/joaquin/Facu/TP4_SISTCOMP/TP4-Sistcomp/TP4-SistComp/loaded_modules_fede.txt'
file3 = '/home/joaquin/Facu/TP4_SISTCOMP/TP4-Sistcomp/TP4-SistComp/loaded_modules_santi.txt'
diff_file = '/home/joaquin/Facu/TP4_SISTCOMP/TP4-Sistcomp/TP4-SistComp/diff.txt'

# Compara los archivos dos a dos
diff1_2 = compare_files(file1, file2)
diff1_3 = compare_files(file1, file3)
diff2_3 = compare_files(file2, file3)

# Escribe las diferencias en el mismo archivo de texto
write_diff(diff1_2, file1, file2, diff_file)
write_diff(diff1_3, file1, file3, diff_file)
write_diff(diff2_3, file2, file3, diff_file)