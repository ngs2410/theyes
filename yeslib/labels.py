CATEGORIES = [
	'TOPS',
	'DRESS',
	'PANT',
	'SKIRT',
	'SHORTS',
	'LINGERIE',
	'OUTERWEAR',
	'JUMPSUIT',
	'JEWELRY',
	'BAG',
	'SHOE',
	'OTHERS',
]
CATEGORY_TO_IDX = {category: idx for idx, category in enumerate(CATEGORIES)}
LABELS = {
	'TOPS': [
		'045f0c5dd2e8307f9480499ad110410fa7515e8a.jpg',
		'8629d5dd9ab4aa34ea2f03dd0066e2f011810a30.jpg',
		'08e4322859724bd259c2b70560f322de095995d2.jpg',
		'60e8b417dd1825d7a0b389711d26a355a53210eb.jpg',
		'1bd13bbd13f6f714eccf3a28ca03887b6393696e.jpg',

		'c0d1f3f33da2130f42b6d18d1b1516c907fdc2d4.jpg',  # Confused with SHORTS
		'6a79d4521ef7a5b82f008a6305699096abc1ba05.jpg',  # Confused with JEWELRY
		'8338fe5c0b9f414295c1e10691e36ddc03f42d22.jpg',  # Confused with BAG
		'b489814a650f8c38259de16b7057750692e604ea.jpg',  # Confused with OTHERS
		'20ea21f0ef0a2250215982a702f41530e62ba227.jpg',  # Confused with JEWELRY
		'692eac2588c787659cd65184f919bf9f66d5f5b2.jpg',  # Confused with DRESS
		'7292f0b6bf42b79d79b0fa6775a4d83e6d71657c.jpg',  # Confused with PANT
		'62193acf429f4156a9ec77400287e6fa9e36a6cb.jpg',  # Confused with DRESS
		'5d98a31763679994612b1172d0fe50edbf7b15b0.jpg',  # Confused with BAG
		'd35dc566420b8d9479c3859ead684753feec6423.jpg',  # Confused with OTHERS
		'3cbb1114dfad62c4fc60eb1a7861ea29c5879cdf.jpg',  # Confused with OTHERS
		'420ad8ab2185ba7f73d7f926cb7e045ce59c702d.jpg',  # Confused with DRESS
		'209838d30237aae80244298824dcac23a470349a.jpg',  # Confused with DRESS
		'fe40ac448b70be651369ea290356c531372cf10a.jpg',  # Confused with OUTERWEAR
		'71c6b052278f75583fca8aa0113d09bef57ac58c.jpg',  # Confused with OUTERWEAR
		'cd18524c9b1e1edefddf7f8987edf9b98a2ce0b0.jpg',  # Confused with DRESS
		'cab97ce2e54c5f6b5eafff6c710831bacb9438d8.jpg',  # Confused with SHORTS
	],
	'DRESS': [
		'9cb6785824b5189e65550a26f789773520152eeb.jpg',
		'6526693997986973fad881ca4cf13888ad223b6c.jpg',
		'a14d01e2e0f70eb1d627fc91696e7c02854b05cd.jpg',
		'a1e522c7881184481da7a9dcc8f9daf904cdcc4a.jpg',
		'b58ba1ec2b1dd3f15ec2ad043cbd3901a9b488ee.jpg',

		'f6a5f1d265225c3ebaf4a2938c9ad117218b695f.jpg',  # Confused with SKIRT
		'cba8aec76576016aecc5dcfaac4b961e04c74911.jpg',  # Confused with BAG
		'bf829c2039d5bafa96756fdabee7009cdfaa38d4.jpg',  # Confused with TOPS
		'a66f35d536d71c6a0e34842a92774a47b180451a.jpg',  # Confused with TOPS
		'4de9bd6c7e9df4ac7a65fe3f9b08d194ae0fdda8.jpg',  # Confused with SKIRT
		'b02b717277fa99866e855da8ca4cf70e47c3ade5.jpg',  # Confused with PANT
		'4256c517dfce2aa1d82d0446969d8273bb133e13.jpg',  # Confused with SKIRT
		'60ef9dec16fe0ef75bdf165805bb46813db08499.jpg',  # Confused with SKIRT
		'fdd8261cac86efc66aed06d6154286c17a93176a.jpg',  # Confused with SKIRT
		'765f1352ba1e2d3ff2437c25a35c750d7551dfda.jpg',  # Confused with OUTERWEAR
		'd25ce6c1f696a7ec9ecff7a873ac3a82bf9a26d9.jpg',  # Confused with BAG
		'093f95a48c807ef5f447cc0c8951f6b2c2fe8a24.jpg',  # Confused with OUTERWEAR
		'2429c1f8ed51d6de1d24555725278787ba495bf0.jpg',  # Confused with OUTERWEAR
	],
	'PANT': [
		'c10729eccc55d98f3d385635dbe88270301d5b83.jpg',
		'cb3d038c13c0d51bf9a15139d90d231e755add51.jpg',
		'760cd0001808aef2c83eeb0ab923d3cd3bf6cebf.jpg',
		'52aa25ff9f4d91a1f2390d670ffb4c1f67f8d912.jpg',
		'782023178a51f480c355047824ab98ec825d8455.jpg',

		'3b92058759db25738303dbce5a4f90f11cdffa67.jpg',  # Confused with OUTERWEAR
		'b8a7529e463c25ab08ad9fa7fc80f55f1a268fcd.jpg',  # Confused with DRESS
		'e0299aa3b1b4f45fbff7e680c33a64293618cdbd.jpg',  # Confused with TOPS
		'bbd75b75c24708095fb5b6f0704257854cd34ef8.jpg',  # Confused with SHORTS
		'f4e384277b09aaac35d3b42b4286c022a5db5135.jpg',  # Confused with BAG
		'231d40069ff7212907b6e06345df2413411ef2f9.jpg',  # Confused with BAG
		'c4857538f1c3a2dda9a119d898cf087681b272e2.jpg',  # Confused with LINGERIE
		'652f8176db106ca53fa4f6a8a1bd3ffac2f8da63.jpg',  # Confused with SKIRT
		'389fd5e0d2ba092c13ff108d55987bce4db59b6c.jpg',  # Confused with SKIRT

	],
	'SKIRT': [
		'89320fb48a4359e94243642c2d6155e42c3318cc.jpg',
		'b855e8422e261c6336e144ff32a923815715886f.jpg',
		'ee58f9951d2cec15d33c816e728cbe63c240c264.jpg',
		'0c1de8f33d47bf84ed289d1cdd40c42938a3668e.jpg',
		'87c1339ac12296177cbdcbd05e23ed4184bff159.jpg',

		'303a605a9e2f2b768e7f24d3e3ec98b9b0a473e2.jpg',  # Confused with DRESS
		'5feaf185f80018bae902bd980931387e0bbc6a1b.jpg',  # Confused with DRESS
	],
	'SHORTS': [
		'3f8745812184a3ec44bb9f7376b8c6d456b0e9e9.jpg',

		'632e2976cd79814bc6bfc76579eed5d2e66e045f.jpg',  # Confused with TOPS
		'414c08db1d974b77a2d991fd81d4e9909cc052c6.jpg',  # Confused with PANT

	],
	'LINGERIE': [
		'24f5c909637775e10f61c3df20c8fb0baf233b63.jpg',
		'4377351f5f58cd72cb8a79b4a97d0b682b44c18d.jpg',
		'8e0f8352a5eec4005cb7672f6753419eb62d8e42.jpg',
		'7a188d42d21146c519c8f8bbf3e4ec1eeaf019fd.jpg',
	],
	'OUTERWEAR': [
		'6f8e82d6f776927a8cdf2df3f38d2ccd47466eae.jpg',
		'9c622bf4405f46f428219d47a5bfdbf3bceb9b75.jpg',
		'ce1dedced8cb6bed26ed8abf9524277a08ebb6ea.jpg',
		'963991cdd627490d08e056c1f7556879761b42a9.jpg',
		'4fbd4afe1d97ef8556cf2c739589b971bfb0a1f2.jpg',

		'e2927a194b5eeae05eb00d67dfb59ec81984a347.jpg',  # Confused with PANT
		'65160f734afef96a1668102691fe9f3c8f870d89.jpg',  # Confused with PANT
		'd8b315a9f1fba7acf9cae6df3aa28b3fa6aa6977.jpg',  # Confused with BAG
		'37776becd71ffa3ea4051e34226ccf442ca53958.jpg',  # Confused with BAG
		'f11cb460f91afb8e41a73ac0c688c0587dca1532.jpg',  # Confused with DRESS
		'a40ed39850e3c7c712c2e16a193f3ccd904df1d4.jpg',  # Confused with PANT
		'9a4611c4b50dc3b309d9f3132940e7f7817b5fee.jpg',  # Confused with PANT
	],
	'JUMPSUIT': [
		'8b167740bc0fa627f555149284df50f5d89f3d2f.jpg',
		'e7ea54507a4668dacd9d5388efeef3680b2e9d19.jpg',
		'6fa29e254cd7501e72242a0ac7e839130a92912c.jpg',
	],
	'JEWELRY': [
		'd3bee9252cf1c06f9287cfbb2b85ef9104b991fd.jpg',
		'dd73d5984fac70eb50598f5473aacb7d70495b82.jpg',
		'673912f770074b00d1a4f3de689c008dabead7a2.jpg',
		'c41e5a98698103b50eaa05fce9748aa73bd7f51a.jpg',
		'42660d5704a7989b709409ecdc26ba25b8a42e8c.jpg',

		'62f9a7fed3ae687b12b253de85cc43b93a6a9707.jpg',  # Confused with OTHERS
		'c3bbe302608dbc72b00f5532ae80abfc26152854.jpg',  # Confused with SHOE
		'd3216cf7343f98a8cb3f856d72df15fd56c74334.jpg',  # Confused with OTHERS
	],
	'BAG': [
		'd2c33b5e8c4fa777adca1bbfec74261eaa30d3ce.jpg',
		'216dd9c11a2e3ab49fd08cc3af36c11ae754c371.jpg',
		'a244637427d66b50b8eed9451968e149cd130b51.jpg',
		'3f6cde8f969ddf13a87a8b547d2068a1d399af77.jpg',
		'5a05c6a7540efe90c8c789f19d333f8d9a5095d7.jpg',
		'1abd3eb7ca37fa1f32fda2b367258458272e18b7.jpg',

		'1876830e04d223f436292f9df68e1adaefb5a0cc.jpg',  # Confused with SHORTS
		'e2d2696058fc4c1038536bef7adbea65a2a58d4d.jpg',  # Confused with OTHERS
		'ab17ff456269a7bf8e78dd657c1252a79af5c8f4.jpg',  # Confused with TOPS
		'0063ded7f70e8d25d952b36c080ef849acea9fca.jpg',  # Confused with TOPS
		'3abc377b9222055c95b7133f9b9f976778abe183.jpg',  # Confused with OTHERS
		'd4e209340ec6a426b529d80159f50e1c16daab23.jpg',  # Confused with SKIRT
		'd50f276650cccbfb50574f624035b9d4e7335319.jpg',  # Confused with OTHERS
		'303d7200cece9d716ea07c9b8a4ef9db9ae49811.jpg',  # Confused with PANT
		'4dd2ef8fba877ef8e442cffe1d7101ef6bb54d1e.jpg',  # Confused with SHOE
		'266fe0b5018b6f189665388e6bf009f17671e1a9.jpg',  # Confused with OUTERWEAR
		'9a8a93a95c32819127316f9b0c0c6d6c9c05ac1a.jpg',  # Confused with OTHERS
		'2c8579abfd400bec59cd633e06c2dcf80331645d.jpg',  # Confused with JUMPSUIT
		'e899bb844c11facf458dc744d2da5705e6e6f6e5.jpg',  # Confused with OUTERWEAR
		'ca144805f846a09e4710ce361b84886ffd7d5397.jpg',  # Confused with OUTERWEAR
		'83620cc8127c6f2d9fa3814a4881f0d1b5e5bf4f.jpg',  # Confused with OUTERWEAR
		'c5ec7d66df21d42b1b7d1b669dd970082146f717.jpg',  # Confused with DRESS
		'b04b854474cfd4d3acb69a8428b31bf1d4e1542b.jpg',  # Confused with SHOE
		'314a0224b09228d52dbae9e8907bb873cb04a0a1.jpg',  # Confused with OUTERWEAR
	],
	'SHOE': [
		'c366c96cff0b7aa0366b393df41484d312a4e6c7.jpg',
		'd6824ebcf95c883a8e83bfa77810e63ae0d9e6b6.jpg',
		'beaf8a22aa6f7d2225ad1fdba45947c6466f1c4b.jpg',
		'1c2c88f53ac9c3e5a4cdf4e6e3799e905b588b37.jpg',
		'abddfc7a8bb3922aac47d37edbabda01da8d1718.jpg',

		'e8886dbecec6199d67fe01476c9873961d532cba.jpg',  # Confused with OTHERS
		'b8e048d07f2799483d4a95a55e8cadaccf163393.jpg',  # Confused with TOPS
		'a9fac9325be598d5cd1acfe410765f831f7b5991.jpg',  # Confused with OTHERS
		'2149632f5c7e558476516fefab551ff4b53164a1.jpg',  # Confused with OTHERS
		'0955d0d908e9c51eb87894b58995f03422c697f7.jpg',  # Confused with BAG
	],
	'OTHERS': [
		'b8376fd0a8d89c2ee3785ba8a0761247f52f5c76.jpg',  # Hat
		'52c24f965467fe2cab7e525eb276f0778003f2b2.jpg',  # Belt
		'b225c4616042ef00765d952346cdda44e5890ce6.jpg',  # Sunglasses
		'a72a26f36bad84dfdf3d7d780569545d3ea4d9b4.jpg',  # Sunglasses
		'2a995179e7907a715ba2cdbbd8a24404041ae7f1.jpg',  # Belt
		'2b8b872057dbcc5b49cf73a495c0b6ff44e77eb8.jpg',  # Gloves
		'cf2a860e318d89f83877c085b38869ef13c29c47.jpg',  # Swimwear
		'3f0b665222a6c1064a3d13ec445e58d3b5e2ead0.jpg',  # Perfume
		'5b07fa1a5e3b630c08aadc0b9ba128084513e47c.jpg',  # Scarf
		'ee6c4d08ca334419fc41da34582ff4b7fac1616c.jpg',  # Tray
		'476111bc257b0de4783ad2b05aa6cdb1e4c1e55e.jpg',  # Phone case

		'f03508a31951cdcc2a8a1df0caea965d751a3960.jpg',  # Phone case - Confused with BAG
		'9a9e488699469f44e70cb7fef7e345984c394a60.jpg',  # Glasses - Confused with JEWELRY
		'f88859d4d14030380f9a99cea94dffcc620787af.jpg',  # Glasses - Confused with TOPS
		'000677ce2c30776c4907492940d2ba810f57bbd8.jpg',  # Luggage label - Confused with BAG
		'276a076d55585e1b27d14e1db748e34df1328c09.jpg',  # Perfume - Confused with BAG
		'2c611f63d1c02ddaf5603e80143c677a26a08502.jpg',  # Tray - Confused with JEWELRY
		'8088bf050528fe84ac39fa8fdfaeedf6a759b029.jpg',  # Swimwear - Confused with BAG
		'531b5f7edb6488610ae2f9c935cc1454fc08a7ef.jpg',  # Belt - Confused with BAG
		'c6f567a846a64444e73084d90c3a150af89f2f61.jpg',  # Scarf - Confused with BAG
		'51bf13ea84fc683276d4292f60cd5cf1d0ab1f3b.jpg',  # Swimwear - Confused with LINGERIE
		'c694ed4969dd7c319b0c12de31900bb4754b6541.jpg',  # Gloves - Confused with BAG
		'b767ed524f50002310671fb6ba1bff90da0bff78.jpg',  # Glasses - Confused with OUTERWEAR

		'5af2425f7cd6b09e3c8b2a6e56829eb4a1feb370.jpg',  # Ambiguous - no description
	],
}
KEY_TO_CATEGORY_IDX = {}
for category, product_list in LABELS.items():
	for product_id in product_list:
		KEY_TO_CATEGORY_IDX[product_id] = CATEGORY_TO_IDX[category]
