import pstats
import sys
sys.path

ps = pstats.Stats("E:\\duke_summary_python\\resourse_files\\result.out")
ps.print_stats()


