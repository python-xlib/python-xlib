# Feed cc -E /usr/include/X11/Xproto.h into this

BEGIN {
  in_struct = 0;

  types[BOOL] = types[BYTE] = 1;
  types[INT8] = types[CARD8] = 1;
  types[INT16] = types[CARD16] = 1;
  types[INT32] = types[CARD32] = 1;
}

in_struct == 1 && $1 == "}" && $2 ~ /x.*;/ {
  name = substr($2, 2, length($2) - 2);

  memlist = "";
  for (i = 0; i < memcount; i++)
    memlist = memlist " " members[i];

  # print name ", " memlist
    
  if (name ~ /Req$/)
    requests[substr(name, 1, length(name) - 3)] = memlist;
  else if (name ~ /Reply$/)
    replies[substr(name, 1, length(name) - 5)] = memlist;
  else
    structs[name] = memlist;

  delete members;
  in_struct = 0;
}

in_struct == 2 && $1 == "}" && $2 == "xEvent;" {
    in_struct = 0;
}

in_struct == 1 && $1 != "}" {
  fcount = split($0, f, "[ \t,;]+");

  if (fcount > 0) {
    if (f[1] == "")
      i = 2;
    else
      i = 1;

    if (next_type == "") {
      type = f[i];
      i++;
    } else {
      type = next_type;
    }

    if ($0 ~ /;[ \t]*$/) {
      next_type = "";
    } else {
      next_type = type;
    }

    for (; i < fcount; i++) {
      members[memcount] = type ":" f[i];
      memcount++;
    }
  }
}

/^typedef struct.*\{/  {
  if (in_struct)
    {
      print "typedef struct while in_struct!";
      exit 1;
    }

  next_type = "";
  in_struct = 1;
  memcount = 0;

    # hack to skip _xEvent
    if ($3 == "_xEvent")
	in_struct = 2;
}

/^typedef x.* x.*;/ {
  if (in_struct)
    {
      print "typedef xFoo xBar; while in_struct!";
      exit 1;
    }

  src = substr($2, 2);
  dest = substr($3, 2, length($3) - 2);

  if (src ~ /Req$/)
      memlist = requests[substr(src, 1, length(src) - 3)];
  else if (src ~ /Reply$/)
      memlist = replies[substr(src, 1, length(src) - 5)];
  else
      memlist = structs[src];

  if (dest ~ /Req$/)
    requests[substr(dest, 1, length(dest) - 3)] = memlist;
  else if (dest ~ /Reply$/)
    replies[substr(dest, 1, length(dest) - 5)] = memlist;
  else
    structs[dest] = memlist;
}

END {
  for (x in requests)
    print "REQUEST " x " " requests[x];
  for (x in replies)
    print "REPLY " x " " replies[x];
  for (x in structs)
    print "STRUCT " x " " structs[x];
}
      
