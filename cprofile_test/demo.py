import pstats
import sys
sys.path

# ps = pstats.Stats("E:\\duke_summary_python\\resourse_files\\result.out")
ps = pstats.Stats("E:\\duke_summary_python\\resourse_files\\myapp.profile")
ps.sort_stats("cumtime")
ps.print_stats()
