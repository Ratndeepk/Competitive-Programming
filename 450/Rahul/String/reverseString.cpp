string reverseWord(string str){
  string strTemp = "";
  for(int i=str.length()-1; i >=0 ; i-- )
    strTemp += str[i];
  return strTemp;
}