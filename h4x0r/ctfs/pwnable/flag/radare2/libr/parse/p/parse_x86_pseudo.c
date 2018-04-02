/* radare - LGPL - Copyright 2009-2017 - nibble, pancake */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <r_lib.h>
#include <r_util.h>
#include <r_anal.h>
#include <r_parse.h>
// 16 bit examples
//    0x0001f3a4      9a67620eca       call word 0xca0e:0x6267
//    0x0001f41c      eabe76de12       jmp word 0x12de:0x76be [2]
//    0x0001f56a      ea7ed73cd3       jmp word 0xd33c:0xd77e [6]
static int replace (int argc, char *argv[], char *newstr) {
#define MAXPSEUDOOPS 10
	int i, j, k, d;
	char ch;
	struct {
		char *op;
		char *str;
		int args[MAXPSEUDOOPS];  // XXX can't use flex arrays, all unused will be 0
	} ops[] = {
		{ "adc",  "# += #", {1, 2}},
		{ "add",  "# += #", {1, 2}},
		{ "and",  "# &= #", {1, 2}},
		{ "call", "# ()", {1}},
		{ "cmove", "if (!var) # = #", {1, 2}},
		{ "cmovl","if (var < 0) # = #", {1, 2}},
		{ "cmp", "var = # - #", {1, 2}},
		{ "cmpsq", "var = # - #", {1, 2}},
		{ "cmpsb", "while (CX != 0) { var = *(DS*16 + SI) - *(ES*16 + DI); SI++; DI++; CX--; if (!var) break; }", {0}},
		{ "cmpsw", "while (CX != 0) { var = *(DS*16 + SI) - *(ES*16 + DI); SI+=4; DI+=4; CX--; if (!var) break; }", {0}},
		{ "dec",  "#--", {1}},
		{ "div",  "# /= #", {1, 2}},
		{ "fabs",  "abs(#)", {1}},
		{ "fadd",  "# = # + #", {1, 1, 2}},
		{ "fcomp",  "var = # - #", {1, 2}},
		{ "fcos",  "# = cos(#)", {1, 1}},
		{ "fdiv",  "# = # / #", {1, 1, 2}},
		{ "fiadd",  "# = # / #", {1, 1, 2}},
		{ "ficom",  "var = # - #", {1, 2}},
		{ "fidiv",  "# = # / #", {1, 1, 2}},
		{ "fidiv",  "# = # * #", {1, 1, 2}},
		{ "fisub",  "# = # - #", {1, 1, 2}},
		{ "fnul",  "# = # * #", {1, 1, 2}},
		{ "fnop",  " ", {0}},
		{ "frndint",  "# = (int) #", {1, 1}},
		{ "fsin",  "# = sin(#)", {1, 1}},
		{ "fsqrt",  "# = sqrt(#)", {1, 1}},
		{ "fsub",  "# = # - #", {1, 1, 2}},
		{ "fxch",  "#,# = #,#", {1, 2, 2, 1}},
		{ "idiv",  "# /= #", {1, 2}},
		{ "imul",  "# *= #", {1, 2}},
		{ "in",   "# = io[#]", {1, 2}},
		{ "inc",  "#++", {1}},
		{ "ja", "if (((unsigned) var) > 0) goto #", {1}},
		{ "jb", "if (((unsigned) var) < 0) goto #", {1}},
		{ "jbe", "if (((unsigned) var) <= 0) goto #", {1}},
		{ "je", "if (!var) goto #", {1}},
		{ "jg", "if (var > 0) goto #", {1}},
		{ "jge", "if (var >= 0) goto #", {1}},
		{ "jle", "if (var <= 0) goto #", {1}},
		{ "jmp",  "goto #", {1}},
		{ "jne", "if (var) goto #", {1}},
		{ "lea",  "# = #", {1, 2}},
		{ "mov",  "# = #", {1, 2}},
		{ "movsd",  "# = #", {1, 2}},
		{ "movsx","# = #", {1, 2}},
		{ "movsxd","# = #", {1, 2}},
		{ "movzx", "# = #", {1, 2}},
		{ "movntdq", "# = #", {1, 2}},
		{ "movnti", "# = #", {1, 2}},
		{ "movntpd", "# = #", {1, 2}},
		{ "mul",  "# *= #", {1, 2}},
		{ "neg",  "# ~= #", {1, 1}},
		{ "nop",  "no operation", {0}},
		{ "not",  "# = !#", {1, 1}},
		{ "or",   "# |= #", {1, 2}},
		{ "out",  "io[#] = #", {1, 2}},
		{ "pop",  "pop #", {1}},
		{ "push", "push #", {1}},
		{ "ret",  "return", {0}},
		{ "sal",  "# <<= #", {1, 2}},
		{ "sar",  "# >>= #", {1, 2}},
		{ "sete",  "# = e", {1}},
		{ "setne",  "# = ne", {1}},
		{ "shl",  "# <<<= #", {1, 2}},
		{ "shld",  "# <<<= #", {1, 2}},
		{ "sbb",  "# = # - #", {1, 1, 2}},
		{ "shr",  "# >>>= #", {1, 2}},
		{ "shlr",  "# >>>= #", {1, 2}},
		//{ "strd",  "# = # - #", {1, 2, 3}},
		{ "sub",  "# -= #", {1, 2}},
		{ "swap", "var = #; # = #; # = var", {1, 1, 2, 2}},
		{ "test", "var = # & #", {1, 2}},
		{ "xchg",  "#,# = #,#", {1, 2, 2, 1}},
		{ "xadd",  "#,# = #,#+#", {1, 2, 2, 1, 2}},
		{ "xor",  "# ^= #", {1, 2}},
		{ NULL }
	};

	if (argc > 2 && !strcmp (argv[0], "xor")) {
		if (!strcmp (argv[1], argv[2])) {
			argv[0] = "mov";
			argv[2] = "0";
		}
	}
	for (i = 0; ops[i].op != NULL; i++) {
		if (!strcmp (ops[i].op, argv[0])) {
			if (newstr != NULL) {
				d = 0;
				j = 0;
				ch = ops[i].str[j];
				for (j = 0, k = 0; ch != '\0'; j++, k++) {
					ch = ops[i].str[j];
					if (ch == '#') {
						if (d >= MAXPSEUDOOPS) {
							// XXX Shouldn't ever happen...
							continue;
						}
						int idx = ops[i].args[d];
						d++;
						if (idx <= 0) {
							// XXX Shouldn't ever happen...
							continue;
						}
						const char *w = argv[idx];
						if (w != NULL) {
							strcpy (newstr + k, w);
							k += strlen (w) - 1;
						}
					} else {
						newstr[k] = ch;
					}
				}
				newstr[k] = '\0';
			}
			return true;
		}
	}

	/* TODO: this is slow */
	if (newstr != NULL) {
		newstr[0] = '\0';
		for (i=0; i<argc; i++) {
			strcat (newstr, argv[i]);
			strcat (newstr, (i == 0 || i== argc - 1)?" ":",");
		}
	}
	return false;
#undef MAXPSEUDOOPS
}

static int parse (RParse *p, const char *data, char *str) {
	char w0[256], w1[256], w2[256], w3[256];
	int i;
	size_t len = strlen (data);
	int sz = 32;
	char *buf, *ptr, *optr, *end;
	if (len >= sizeof (w0) || sz >= sizeof (w0)) {
		return false;
	}
	// strdup can be slow here :?
	if (!(buf = strdup (data))) {
		return false;
	}
	if (!strncasecmp (buf, "lea", 3)) {
		r_str_replace_char (buf, '[', 0);
		r_str_replace_char (buf, ']', 0);
	}
	if (*buf) {
		*w0 = *w1 = *w2 = *w3 = '\0';
		end = strchr (buf, '\0');
		ptr = strchr (buf, ' ');
		if (!ptr) {
			ptr = strchr (buf, '\t');
		}
		if (!ptr) {
			ptr = end;
		}
		*ptr = '\0';
		if (ptr != end) for (++ptr; *ptr == ' '; ptr++);
		r_str_ncpy (w0, buf, sizeof (w0));
		r_str_ncpy (w1, ptr, sizeof (w1));
		optr = ptr;
		ptr = strchr (ptr, ',');
		if (ptr) {
			*ptr = '\0';
			for (++ptr; *ptr == ' '; ptr++);
			r_str_ncpy (w1, optr, sizeof (w1));
			r_str_ncpy (w2, ptr, sizeof (w2));
			optr = ptr;
			ptr = strchr (ptr, ',');
			if (ptr) {
				*ptr = '\0';
				for (++ptr; *ptr == ' '; ptr++);
				r_str_ncpy (w2, optr, sizeof (w2));
				r_str_ncpy (w3, ptr, sizeof (w3));
			}
		}
	}
	char *wa[] = { w0, w1, w2, w3 };
	int nw = 0;
	for (i = 0; i < 4; i++) {
		if (wa[i][0] != '\0') {
			nw++;
		}
	}
	if (strstr (w0, "mul") && nw == 2 ) {
		r_str_ncpy (wa[2], wa[1], sizeof (w2));

		switch (wa[2][0]) {
		case 'q':
		case 'r': //qword, r..
			r_str_ncpy (wa[1], "rax", sizeof (w1));
			break;
		case 'd':
		case 'e': //dword, e..
			if (strlen (wa[2]) > 2) {
				r_str_ncpy (wa[1], "eax", sizeof (w1));
				break;
			}
		default : // .x, .p, .i or word
			if (wa[2][1] == 'x' || wa[2][1] == 'p' || \
				wa[2][1] == 'i' || wa[2][0] == 'w') {
				r_str_ncpy (wa[1], "ax", sizeof (w1));
			} else { // byte and lowest 8 bit registers
				r_str_ncpy (wa[1], "al", sizeof (w1));
			}
		}
		replace (nw, wa, str);
	} else if ((strstr (w1, "ax") || strstr (w1, "ah") || strstr (w1, "al")) && !p->retleave_asm) {
		if (!(p->retleave_asm = (char *) malloc (sz))) {
			return false;
		}
		r_snprintf (p->retleave_asm, sz, "return %s", w2);
		replace (nw, wa, str);
	} else if ((strstr (w0, "leave") && p->retleave_asm) || (strstr (w0, "pop") && strstr (w1, "bp"))) {
		r_str_ncpy (wa[0], " \0", 2);
		r_str_ncpy (wa[1], " \0", 2);
		replace (nw, wa, str);
	} else if (strstr (w0, "ret") && p->retleave_asm) {
		r_str_ncpy (str, p->retleave_asm, sz);
		R_FREE (p->retleave_asm);
	} else if (p->retleave_asm) {
		R_FREE (p->retleave_asm);
		replace (nw, wa, str);
	} else {
		replace (nw, wa, str);
	}
	free (buf);
	return true;
}

#if 0
static inline int ishexch (char c) {
	if (c>=0 && c<=9) return 1;
	if (c>='a' && c<='f') return 1;
	if (c>='A' && c<='F') return 1;
	return 0;
}

static inline int issegoff (const char *w) {
	if (!ishexch (w[0])) return 0;
	if (!ishexch (w[1])) return 0;
	if (!ishexch (w[2])) return 0;
	if (!ishexch (w[3])) return 0;
	// :
	if (!ishexch (w[5])) return 0;
	if (!ishexch (w[6])) return 0;
	if (!ishexch (w[7])) return 0;
	if (!ishexch (w[8])) return 0;
	return 1;
}
#endif

static void parse_localvar (RParse *p, char *newstr, size_t newstr_len, const char *var, const char *reg, char sign, bool att) {
	if (att) {
		if (p->localvar_only) {
			snprintf (newstr, newstr_len - 1, "%s", var);
		} else {
			snprintf (newstr, newstr_len - 1, "%s(%%%s)", var, reg);
		}
	} else {
		if (p->localvar_only) {
			snprintf (newstr, newstr_len - 1, "[%s]", var);
		} else {
			snprintf (newstr, newstr_len - 1, "[%s %c %s]", reg, sign, var);
		}
	}
}

static inline void mk_reg_str(const char *regname, int delta, bool sign, bool att, char *dest, int len) {
	if (att) {
		if (delta < 10) {
			snprintf (dest, len - 1, "%s%d(%%%s)", sign ? "" : "-", delta, regname);
		} else {
			snprintf (dest, len - 1, "%s0x%x(%%%s)", sign ? "" : "-", delta, regname);
		}
	} else {
		if (delta < 10) {
			snprintf (dest, len - 1, "[%s %c %d]", regname, sign ? '+':'-', delta);
		} else {
			snprintf (dest, len - 1, "[%s %c 0x%x]", regname, sign ? '+':'-', delta);
		}
	}
}

static bool varsub (RParse *p, RAnalFunction *f, ut64 addr, int oplen, char *data, char *str, int len) {
	RList *regs, *bpargs, *spargs;
	RAnalVar *reg, *bparg, *sparg;
	RListIter *regiter, *bpargiter, *spiter;
	char oldstr[64], newstr[64];
	char *tstr = strdup (data);
	if (!tstr) {
		return false;
	}

	bool att = strchr (data, '%');

	if (p->relsub) {
		if (att) {
			char *rip = (char *) r_str_casestr (tstr, "(%rip)");
			if (rip) {
				*rip = 0;
				char *pre = tstr;
				char *pos = rip + 6;
				char *word = rip;
				while (word > tstr && *word != ' ') {
					word--;
				}

				if (word > tstr) {
					*word++ = 0;
					*rip = 0;
					st64 n = r_num_math (NULL, word);
					ut64 repl_num = oplen + addr + n;
					char *tstr_new = r_str_newf ("%s 0x%08"PFMT64x"%s", pre, repl_num, pos);
					*rip = '(';
					free (tstr);
					tstr = tstr_new;
				}
			}
		} else {
			char *rip = (char *) r_str_casestr (tstr, "[rip");
			if (rip) {
				char *ripend = strchr (rip + 3, ']');
				const char *plus = strchr (rip, '+');
				const char *neg = strchr (rip, '-');
				char *tstr_new;
				ut64 repl_num = oplen + addr;

				if (!ripend) {
					ripend = "]";
				}
				if (plus) {
					repl_num += r_num_get (NULL, plus + 1);
				}
				if (neg) {
					repl_num -= r_num_get (NULL, neg + 1);
				}

				rip[1] = '\0';
				tstr_new = r_str_newf ("%s0x%08"PFMT64x"%s", tstr, repl_num, ripend);
				free (tstr);
				tstr = tstr_new;
			}
				if (!strncasecmp (tstr, "lea", 3)) {
					r_str_replace_char (tstr, '[', 0);
					r_str_replace_char (tstr, ']', 0);
				}
		}
	}

	if (!p->varlist) {
                free (tstr);
		return false;
        }
	regs = p->varlist (p->anal, f, 'r');
	bpargs = p->varlist (p->anal, f, 'b');
	spargs = p->varlist (p->anal, f, 's');
	/*iterate over stack pointer arguments/variables*/
	bool ucase = *tstr >= 'A' && *tstr <= 'Z';
	if (ucase && tstr[1]) {
		ucase = tstr[1] >= 'A' && tstr[1] <= 'Z';
	}
	r_list_foreach (spargs, spiter, sparg) {
		// assuming delta always positive?
		mk_reg_str (p->anal->reg->name[R_REG_NAME_SP], sparg->delta, true, att, oldstr, sizeof (oldstr));

		if (ucase) {
			r_str_case (oldstr, true);
		}
		parse_localvar (p, newstr, sizeof (newstr), sparg->name, p->anal->reg->name[R_REG_NAME_SP], '+', att);
		if (ucase) {
			char *plus = strchr (newstr, '+');
			if (plus) {
				*plus = 0;
				r_str_case (newstr, true);
				*plus = '+';
			} else {
				r_str_case (newstr, true);
			}
		}
		char *ptr = strstr(tstr, oldstr);
		if (ptr && (!att || *(ptr - 1) == ' ')) {
			tstr = r_str_replace (tstr, oldstr, newstr, 1);
			break;
		} else {
			r_str_case (oldstr, false);
			ptr = strstr(tstr, oldstr);
			if (ptr && (!att || *(ptr - 1) == ' ')) {
				tstr = r_str_replace (tstr, oldstr, newstr, 1);
				break;
			}
		}
	}
	/* iterate over base pointer args/vars */
	r_list_foreach (bpargs, bpargiter, bparg) {
		char sign = '+';
		if (bparg->delta < 0) {
			sign = '-';
			bparg->delta = -bparg->delta;
		}
		mk_reg_str (p->anal->reg->name[R_REG_NAME_BP], bparg->delta, sign=='+', att, oldstr, sizeof (oldstr));
		if (ucase) {
			r_str_case (oldstr, true);
		}
		parse_localvar (p, newstr, sizeof (newstr), bparg->name, p->anal->reg->name[R_REG_NAME_BP], sign, att);
		if (ucase) {
			char *plus = strchr (newstr, sign);
			if (plus) {
				*plus = 0;
				r_str_case (newstr, true);
				*plus = sign;
			} else {
				r_str_case (newstr, true);
			}
		}
		char *ptr = strstr (tstr, oldstr);
		if (ptr && (!att || *(ptr - 1) == ' ')) {
			tstr = r_str_replace (tstr, oldstr, newstr, 1);
			break;
		} else {
			r_str_case (oldstr, false);
			ptr = strstr(tstr, oldstr);
			if (ptr && (!att || *(ptr - 1) == ' ')) {
				tstr = r_str_replace (tstr, oldstr, newstr, 1);
				break;
			}
		}
		// Try with no spaces
		snprintf (oldstr, sizeof (oldstr)-1, "[%s%c0x%x]", p->anal->reg->name[R_REG_NAME_BP], sign, bparg->delta);
		if (strstr (tstr, oldstr) != NULL) {
			tstr = r_str_replace (tstr, oldstr, newstr, 1);
			break;
		}
	}

	char bp[32];
	if (p->anal->reg->name[R_REG_NAME_BP]) {
		strncpy (bp, p->anal->reg->name[R_REG_NAME_BP], sizeof (bp) - 1);
		if (isupper (*str)) {
			r_str_case (bp, true);
		}
		bp[sizeof (bp) - 1] = 0;
	} else {
		bp[0] = 0;
	}

	r_list_foreach (regs, regiter, reg) {
		RRegItem *r = r_reg_index_get (p->anal->reg, reg->delta);
		if (r && r->name && strstr (tstr, r->name)){
			tstr = r_str_replace (tstr, r->name, reg->name, 1);
		}
	}

	bool ret = true;
	if (len > strlen (tstr)) {
		strncpy (str, tstr, strlen (tstr));
		str[strlen (tstr)] = 0;
	} else {
		// TOO BIG STRING CANNOT REPLACE HERE
		ret = false;
	}
	free (tstr);
	r_list_free (spargs);
	r_list_free (bpargs);
	r_list_free (regs);
	return ret;
}

RParsePlugin r_parse_plugin_x86_pseudo = {
	.name = "x86.pseudo",
	.desc = "X86 pseudo syntax",
	.parse = &parse,
	.varsub = &varsub,
};

#ifndef CORELIB
RLibStruct radare_plugin = {
	.type = R_LIB_TYPE_PARSE,
	.data = &r_parse_plugin_x86_pseudo,
	.version = R2_VERSION
};
#endif