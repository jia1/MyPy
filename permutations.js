function permutations(s) {
    if (!s) {
        return [[]];
    } else {
        return flatmap(function(x) {
            return map(function(p) {
                return pair(x,p);
            },
            permutations(remove(x,s)));
        }, s);
    }
}

// TODO: Fix syntax for the stuff inside else-block.
