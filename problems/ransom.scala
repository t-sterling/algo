object Ransom {

  /** type alias so it's easier to think about */
  type Combination = List[Int]

  def main(args:Array[String]) = {

    // inputs
    val denoms = List(1,2,3,7,70,15)
    val x = 230

    // generate every combination of the denominations which sum to X
    val combos = generateAll(x, denoms.sorted.reverse)

    // sort the combinations by size and return the first (shortest)
    val smallest = combos.reduce((a,b) => if(a!=null && a.size < b.size) a else b)
    println(smallest)

  }


  /** recursively generates all combinations with repetition amd yield a list of them which sum to X */
  def generateAll(x:Int, denom:List[Int]):List[Combination] = {

    var max = -1;

    def inner(acc:Int, combo:Combination, combos:List[Combination]):List[Combination] = acc match {
      case `x` => {
        max = combo.size
        combo :: combos	 // if the combo sums to X then add the combo to the list of combos and return
      }
      case n if n > `x` => combos	// if the combo is greater than X then return without appending the current combo and return
      case _ =>  if( max == -1 || combo.size < max) {
    	  denom.flatMap(d => inner(acc + d, d :: combo, combos))// the sum must be < X - recurse all the sub combos for each denomination and return
      } else {
    	  combos
      }
    }
    inner(0,List(),List())
  }

}