"""Quick import test for the modified hybrid-agent modules."""
import sys
sys.path.insert(0, '.')
from hybrid_agent import run_local_stage, _log_local_failure
print('hybrid_agent.py OK')
from workstation_route import run_workstation_route, build_local_config
print('workstation_route.py OK')
from run_workstation_hybrid_route import main
print('run_workstation_hybrid_route.py OK')
