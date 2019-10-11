__int64 __fastcall sub_100000DB0(
  void (__fastcall *a1)(__int64, __int64),          // sub_100000D00
  unsigned int (__fastcall *a2)(__int64, void *),   // sub_100000C80
  unsigned int (__fastcall *a3)(__int64),           // sub_100000BA0
  unsigned int (__fastcall *a4)(__int64),           // sub_100000C10
  __int64 a5,                                       // scanf address
  __int64 a6)                                       // calloc(0x29BuLL, 4uLL)
{
  unsigned int (__fastcall *v6)(__int64);           // sub_100000BA0
  __int64 v7;                                       // scanf address
  __int64 v9;                                       // calloc(0x29BuLL, 4uLL)
  unsigned int (__fastcall *v10)(__int64);          // sub_100000C10

  v6 = a3;
  v10 = a4;
  v7 = a5;
  v9 = a6;
  a1(calloc, scanf_address);
  if ( a3(scanf_address) && a4(calloc) && a2(calloc, &unk_100001040) )
    printf("Congratz - You have earned it!");
  else
    printf("%s", "You've got to do better");
  return 0LL;
}