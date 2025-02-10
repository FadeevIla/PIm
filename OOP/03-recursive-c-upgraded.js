const get_recursive = (max_w, arr) => {
    const get_combs = (combo, deep) => {
      if (deep === arr.length) {
        combs.push([...combo]);
        return;
      }
      get_combs([...combo, arr[deep]], deep + 1);
      get_combs(combo, deep + 1);
    };
  
    const combs = [];
    get_combs([], 0);
  
    const filtered = combs
      .map(combo => ({
        cur_w: combo.reduce((acc, cur) => acc + cur.w, 0),
        cur_p: combo.reduce((acc, cur) => acc + cur.p, 0),
        combo,
      }))
      .filter(e => e.cur_w <= max_w);
  
    const max_combo = filtered.reduce((a, b) =>
      a.cur_p > b.cur_p ? a : b,
      filtered[0]
    );
  
    return max_combo;
  };