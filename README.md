# Freebie Tracker

## Setup

`pipenv install` will make sure we have ipdb included in our environment.  
`pipenv shell` allows us access to that environment.  

## Introduction

For this assignment, we'll be working with a freebie domain.

As developers, when you attend hackathons, you'll realize they hand out a lot of
free items (informally called _freebies_, or swag)! Let's make an app for
developers that keeps track of all the freebies they obtain.

We have three models: `Company`, `Dev`, and `Freebie`

For our purposes, a `Company` has many `Freebie`s, a `Dev` has many `Freebie`s,
and a `Freebie` belongs to a `Dev` and to a `Company`.

`Company` - `Dev` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Instructions

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This lab does not have tests & we cannot run
`pytest`. You'll need to create your own sample
instances so that you can try out your code on your own. Make sure your
relationships and methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start an `ipdb` session
with your classes defined. You can test out the methods that you write here. 

Writing error-free code is more important than completing all of the
deliverables listed- prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices.


## Deliverables

Write the following functionality in the classes in the files provided. Feel free to
build out any helper methods if needed.

- A `Company` has a name that's a string & founding year that is an integer.

- A `Dev` has a name that's a string.

- A `Freebie` belongs to a `Dev`, and a `Freebie` also belongs to a `Company`.
 
- The `freebies` model should also have:
  - An `item_name` column that stores a string.
  - A `value` column that stores an integer.


**After you've set up your `freebies`**, work on building out the following
deliverables.


#### Freebie

- `Freebie.dev` returns the `Dev` instance for this Freebie.
- `Freebie.company` returns the `Company` instance for this Freebie.

#### Company

- `Company.freebies` returns a collection of all the freebies for the Company.
- `Company.devs` returns a collection of all the devs who collected freebies
  from the company.

#### Dev

- `Dev.freebies` returns a collection of all the freebies that the Dev has collected.
- `Dev.companies`returns a collection of all the companies that the Dev has collected
  freebies from.

Use `python debug.py` and check that these methods work before proceeding. 

### Aggregate Methods

#### Freebie

- `Freebie.print_details()`should return a string formatted as follows:
  `{dev name} owns a {freebie item_name} from {company name}`.

#### Company

- `Company.give_freebie(dev, item_name, value)` takes a `dev` (an instance of
  the `Dev` class), an `item_name` (string), and a `value` as arguments, and
  creates a new `Freebie` instance associated with this company and the given
  dev.
- Class method `Company.oldest_company()`returns the `Company` instance with
  the earliest founding year.

#### Dev

- `Dev.received_one(item_name)` accepts an `item_name` (string) and returns
  `True` if any of the freebies associated with the dev has that `item_name`,
  otherwise returns `False`.
- `Dev.give_away(dev, freebie)` accepts a `Dev` instance and a `Freebie`
  instance, changes the freebie's dev to be the given dev; your code should only
  make the change if the freebie belongs to the dev who's giving it away
