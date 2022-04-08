import itertools as it

# number of ticks in a full rotation
TOT_TICKS = 360 * 12 * 10**10

# speed of hour, minute and second hand in ticks per nanosecond
H_TPNS = 1
M_TPNS = 12
S_TPNS = 720

# number of nanoseconds in other units of time
NS_IN_SEC = 10**9
NS_IN_MIN = 60 * NS_IN_SEC
NS_IN_HR =  60 * NS_IN_MIN

# seconds in 12 hours
S_IN_12H = 12 * 60 * 60

def ns_to_timespec(ns):
    # convert time in nanoseconds to [h, m, s, n]
    h = (ns // NS_IN_HR) % 12
    m = (ns // NS_IN_MIN) % 60
    s = (ns // NS_IN_SEC) % 60
    n = ns % NS_IN_SEC
    return h, m, s, n

def ticks_to_ns(ticks):
    # convert [hour_hand, minute_hand, second_hand] into nanoseconds assuming an upright orientation.
    h_tks = ticks[0]
    ns = h_tks
    return ns

def sec_to_ticks(s):
    # convert a time in seconds to the ticks of the hands of a corresponding clock which is upright.
    ns = s * NS_IN_SEC
    h_tks = (ns * H_TPNS) % TOT_TICKS
    m_tks = (ns * M_TPNS) % TOT_TICKS
    s_tks = (ns * S_TPNS) % TOT_TICKS
    return h_tks, m_tks, s_tks

def normalise_ticks(ticks):
    # rotate the clock represented by ticks until its hour hand is pointing straight up. If two
    # ticks have the same "normal representation" they can be rotated into each other.
    [h_tks, m_tks, s_tks] = ticks
    new_m_tks = (m_tks - h_tks) % TOT_TICKS
    new_s_tks = (s_tks - h_tks) % TOT_TICKS
    return 0, new_m_tks, new_s_tks

def wind_back(ticks, ns):
    # wind the clock with hands at [h, m, s] ticks ns nanoseconds backwards.
    [h_tks, m_tks, s_tks] = ticks
    new_h_tks = (h_tks - ns*H_TPNS) % TOT_TICKS
    new_m_tks = (m_tks - ns*M_TPNS) % TOT_TICKS
    new_s_tks = (s_tks - ns*S_TPNS) % TOT_TICKS
    return new_h_tks, new_m_tks, new_s_tks

def solve(ticks, tspec_dict):
    # solve test set 2 by getting the time in nanoseconds from a dict.
    assigns = it.permutations(ticks)
    for assign in assigns:
        # the second allignment will be preserved by any rotation
        ns = ticks_to_ns(assign)
        remd = ns % NS_IN_SEC
        ticks = wind_back(assign, remd)
        print(ticks)
        nform = normalise_ticks(ticks)
        if nform in tspec_dict.keys():
            res_ns =  tspec_dict[nform] + remd
            return ns_to_timespec(res_ns)
    raise NotImplementedError("We expect every input to actually be a valid time in nanoseconds.")

def create_dict():
    # create a dict where keys is the normal form of every clock with an integer number of seconds, and
    # values is that clock's time as a timespec h, m, s, n.
    res = {}
    for s in range(S_IN_12H):
        ticks = sec_to_ticks(s)
        nform_ticks = normalise_ticks(ticks)
        res[nform_ticks] = s * NS_IN_SEC
    return res

def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def main():
    # before we begin, store all 3*60*60 
    ncases = int(input())
    tspec_of_nform = create_dict()
    for case in range(1, ncases+1):
        ticks = read_intlist()
        [h, m, s, n] = solve(ticks, tspec_of_nform)
        print(f"Case #{case}: {h} {m} {s} {n}")

main()