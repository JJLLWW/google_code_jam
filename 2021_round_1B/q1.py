import itertools as it

# common angles in ticks.
NTICKS_FULL_ROT = 360 * 12 * (10**10)
NTICKS_TWELTH_ROT = 360 * (10**10)
NTICKS_SIXTYTH_ROT = 6 * 12 * (10**10)

# ticks per nanosecond movement of each hand.
SH_TPNS = 720
MH_TPNS = 12
HH_TPNS = 1

# ticks per second movement of each hand.
SH_TPS = SH_TPNS * 10**9
MH_TPS = MH_TPNS * 10**9
HH_TPS = HH_TPNS * 10**9

def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def get_time(hands):
    # get the time given the positions in ticks of each of the hands on a clock
    if len(hands) != 3:
        raise ValueError("get_time: input list does not have length 3")
    [hh_ticks, mh_ticks, sh_ticks] = hands
    n_hrs = hh_ticks // NTICKS_TWELTH_ROT
    n_mins = mh_ticks // NTICKS_SIXTYTH_ROT
    n_secs = sh_ticks // NTICKS_SIXTYTH_ROT
    # seconds hand rotates 720 ticks each nanosecond
    sh_remainder = sh_ticks % NTICKS_SIXTYTH_ROT
    n_nsecs = sh_remainder // SH_TPNS
    return [n_hrs, n_mins, n_secs, n_nsecs]

def rot_salligned_to_upright(ticks):
    # return the ticks of this second alligned clock rotated upright, or None if not possible.
    [h_tks, m_tks, s_tks] = ticks
    # seconds in a day is 12*3600
    for i in range(12*3600):
        if h_tks == m_tks and m_tks == s_tks:
            # this is 12 o'clock, so must be a valid time.
            twelve = h_tks
            rh_tks, rm_tks, rs_tks = 0, 0, 0
            # ! check this
            rh_tks = (ticks[0] - twelve) % NTICKS_FULL_ROT
            rm_tks = (ticks[1] - twelve) % NTICKS_FULL_ROT
            rs_tks = (ticks[2] - twelve) % NTICKS_FULL_ROT
            return rh_tks, rm_tks, rs_tks
        else:
            # beware of wraparound.
            h_tks = (h_tks + HH_TPS) % NTICKS_FULL_ROT
            m_tks = (m_tks + MH_TPS) % NTICKS_FULL_ROT
            s_tks = (s_tks + SH_TPS) % NTICKS_FULL_ROT
    return None

def sec_aligned(ticks):
    # solve a second aligned, potentially rotated clock.
    assigns = it.permutations(ticks)
    for assign in assigns:
        rassign = rot_salligned_to_upright(assign)
        if rassign is not None:
            return get_time(rassign)
    raise(NotImplementedError("we assume the clock is valid"))

# maybe this hackery will continue to work, but there was definitely a smarter way.
def rot_to_salligned(ticks):
    # every clock will eventually become second alligned whether it is valid or not.
    [h_tks, m_tks, s_tks] = ticks
    nsec_passed = 0
    # we have s + nsec_passed * SH_TPNS = m + nsec_passed * MH_TPNS mod NTICKS_FULL_ROT
    nsec_passed = ((m_tks-s_tks)//(SH_TPNS + MH_TPNS)) % NTICKS_FULL_ROT
    return None

def nsec_aligned(ticks):
    # solve a nanosecond aligned potentially rotated clock.
    assigns = it.permutations(ticks)
    for assign in assigns:
        s_ticks = rot_to_salligned(ticks)
    raise(NotImplementedError("we assume the clock is valid"))    

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        ticks = read_intlist()
        [h, m, s, n] = sec_aligned(ticks) 
        print(f"Case #{case}: {h} {m} {s} {n}")

main()