import angr

proj = angr.Project('../c.exe', load_options = {'auto_load_libs': False})

find_addr = 0x00000000004016EF
avoid_addr = [0x0000000000401598, 0x00000000004016A7]

state = proj.factory.entry_state()
sm = proj.factory.simulation_manager(state)
sm.explore(find = find_addr, avoid = avoid_addr)	# avoid 생략 가능

if len(sm.found) > 0:
	print(f'[{sm.found[0].posix.dumps(0)}]')
else:
	print('not found')
