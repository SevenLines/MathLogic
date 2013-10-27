#!/usr/bin/perl -w

use strict;
use warnings;
use diagnostics;
use v5.10;

use Getopt::Std;
use List::Util qw\shuffle\;


my $seed = 777;
my $vars_per_column = 4;
my @letters = qw(x y z s t);
my @quantifiers = ('\forall', '\exists');
my @words = ('red', 'how',
             'one', 'car',
             'two', 'nap',
             'kid', 'man',
             'nya', 'can',
             'nom', 'you',
             'let', 'buy',
             'boy', 'his',
             'gym', 'cap',
             'air', 'sun',
             'ink', 'rat',
             'pal', 'owl',
             'cat', 'way',
             'dog', 'use',
             'key', 'new',
             'she', 'raw',
             'old', 'mad',
             'sea', 'kit',
             'day', 'log',
             'who', 'jet',
              );

my $var_count = @words; # count of vars
srand($seed); # set seed

# gen list of tasks on building prenex form
sub gen_prenex_form_tasks
{
	my $word;
	my @out;
	for (1 .. $var_count) {
		$word = uc $words[ $_ % (scalar @words) ];
		
		my @shuf_letters = shuffle(@letters);
		
		my $task = gen_prenex_form_task({
			q0 => $quantifiers[int(rand(scalar @quantifiers))],
			q1 => $quantifiers[int(rand(scalar @quantifiers))],
			q2 => $quantifiers[int(rand(scalar @quantifiers))],
			q3 => $quantifiers[int(rand(scalar @quantifiers))],
			
			p0 => $shuf_letters[0],
			p1 => $shuf_letters[1],
			p2 => $shuf_letters[2],
			
			l0 => substr($word, 0, 1),
			l1 => substr($word, 1, 1),
			l2 => substr($word, 2, 1),
			
			negPos => $_ % 2,
		});
		push @out, $task;
	}
	return @out;
}

sub gen_prenex_form_task(%)
{
	my %params = %{ (shift) };

	my $q0 = $params{q0}; # first quantifier 
	my $q1 = $params{q1}; # second quantifier 
	my $q2 = $params{q2}; # third quantifier
	my $q3 = $params{q3}; # fourth quantifier
	
	my $p0 = $params{p0} || 'x'; # params like for letters 'x,y' and so on
	my $p1 = $params{p1} || 'y'; 
	my $p2 = $params{p2} || 'z'; 
	
	my $l0 = $params{l0}; # first letter
	my $l1 = $params{l1}; # second letter
	my $l2 = $params{l2}; # third letter
	
	my $negPos = $params{negPos}; #negPos
	return "$q0 $p0$l0($p0,$p1) \\to \\neg $q1 $p1( $l1($p1,$p0) \\wedge $q2 $p0$q3 $p2 $l2($p2, $p0) )";
}

gen_prenex_form_tasks();

# task on predicate building
my %task1 = (
	title => 'Построить предикат:',	
	tasks => [
		'Существование четных чисел.',
		'Существование простых чисел.',
		'Существование бесконечно большого числа.',
		'Существование бесконечно малго положительного числа, большего нуля.',
		'Существование целых чисел.',
		'Существование наибольшего общего делителя.',
		'Существование дробных чисел.',
		'Существование сходящихся последовательностей.',
		'Существование производных. На множестве функций.',
		'Существование суммы двух чисел.',
		'Существование треугольника. На множестве натуральных чисел.',
	],
);


# Привести к предваренной форме методом упрощеной индукции:
my $title = <<END;
Привести к предваренной форме методом упрощеной индукции. 
Напомню что \$A|B = \\neg (A \\wedge B)\$, а \$A\\downarrow B = \\neg (A \\vee B)\$.
END
my %task2 = (
	title => $title,
	tasks => [
		'\forall xA(x)|B',
		'\forall xA(x)\downarrow B',
		'A|\exists xB(x)',
		'A\downarrow\exists xB(x)',
		'\exists xA(x)|B',
		'\exists xA(x)\downarrow B',
		'A|\forall xB(x)',
		'A\downarrow\forall xB(x)',
	],
);

my @tasks = gen_prenex_form_tasks();
my %task3 = (
	title => "Привести к предваренной нормальной форме:\n",
	tasks => \@tasks 
);

# header of latex document
my $header = join("\n",(
	  '\documentclass[9pt,a4paper]{article}',
	  '\usepackage[utf8]{inputenc}',
	  '\usepackage{amsmath}',
	  '\usepackage{amsfonts}',
	  '\usepackage{amssymb}',
	  '\usepackage{multicol}',
	  '\usepackage[russian]{babel}',
	  '\usepackage[left=1.00cm, right=1.00cm, top=1.00cm, bottom=1.00cm]{geometry}',
	  '',
	  '\setlength{\columnsep}{20mm}',
	  '\setlength{\columnseprule}{0.1pt}',
	  '\setlength\parindent{0pt}',
	  '\pagestyle{empty}',
	  '',
	  '\begin{document}',
	  '\begin{multicols}{2}',
        ));

say $header;

#tasks of latex document

my $ln = '\\\\\\\\'; #new paragraph in latex
for ( 1 .. $var_count ) {
  my @tasks;
  my $title;
  say "\\line(1,0){250}$ln\nВариант $_.$ln";

  # first task, on building predicate form
  @tasks = @{ $task1{tasks} };
  $title = $task1{title};
  say "1. $title @tasks[$_ % scalar @tasks]\\\\";
  
  # second task, on prenex form proove using simplified induction
  @tasks = @{ $task2{tasks} };
  $title = $task2{title};
  say "2. $title \$\$@tasks[$_ % scalar @tasks]\$\$";
  
  # third task, on prenex form convert
  @tasks = @{ $task3{tasks} };
  $title = $task3{title};
  say "3. $title \$\$@tasks[$_ % scalar @tasks]\$\$";
  
  if ( $_ % $vars_per_column == 0 ) {
    if ( $_ == $var_count) {
    	# for avoiding page-proofs problems
    	say "\\line(1,0){250}\\vfill"; 
    } else {
    	say "\\line(1,0){250}\\vfill\\columnbreak\n\n";	
    }
  }
}

#footer of latex document
#say "\\line(1,0){250}\\vfill\n\n";
say "\\end{multicols}\n\\end{document}";

