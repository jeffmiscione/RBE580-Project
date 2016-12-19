thumb_length = 65; middle_length = 80; palm_width = 85;

module palm_cover(thumb_length,middle_length,palm_width)
{
    wrist=60;
    res=30;
    difference(){
        union(){
            //palm part
            cube([palm_width*10/85,palm_width*25/85,palm_width*2/85]); 
            translate([0,palm_width*50/85,0])cube([palm_width*10/85,palm_width*35/85,palm_width*2/85]);
            translate([palm_width*75/85,palm_width*50/85,0]) cube([palm_width*10/85,palm_width*35/85,palm_width*2/85]);
            translate([palm_width*50/85,0,0]) cube([palm_width*10/85,palm_width*25/85,palm_width*2/85]);   
            translate([0,0,palm_width*2/85])cube([palm_width,palm_width,palm_width*3/85]);
        }
        union(){
            //thumb section
            translate([palm_width*60/85,0,0])
            cube([palm_width*25/85,palm_width*25/85,palm_width*5/85],false);
            translate([palm_width,palm_width*50/85,0])
            rotate([0,0,-135])
            cube([(palm_width*25/85)/sin(45),palm_width*25/85,palm_width*5/85],false);
        
        //screw holes
        for(i=[0:1:1]){
            translate([palm_width*(5/85+50/85*i),palm_width*5/85,0])
            cylinder(10,r=3.46/2,false,$fn=50);
            translate([palm_width*(5/85+50/85*i),palm_width*20/85,0])
            cylinder(10,r=3.46/2,false,$fn=50);
        }
        for(i=[0:1:1]){
            translate([palm_width*(5/85+75/85*i),palm_width*55/85,0])
            cylinder(10,r=3.46/2,false,$fn=50);
            translate([palm_width*(5/85+75/85*i),palm_width*75/85,0])
            cylinder(10,r=3.46/2,false,$fn=50);
        }

        //internal screws
        translate([palm_width*64.31/85,palm_width*37/85,palm_width*2/85]) cylinder(palm_width*1.24/85,r=2.38/2,true,$fn=res);
        for(i=[0:1:1]){
        translate([palm_width*(22.69+20*i)/85,palm_width*(37-i)/85,palm_width*2/85]) cylinder(palm_width*1.24/85,r=2.38/2,true,$fn=res);
         
        translate([palm_width*(53.5-20*i)/85,palm_width*39/85,palm_width*2/85]) cylinder(palm_width*1.24/85,r=2.38/2,true,$fn=res);

            
        translate([palm_width*(11.69+44*i)/85,palm_width*73/85,palm_width*2/85]) cylinder(palm_width*1.24/85,r=2.38/2,true,$fn=res);
        translate([palm_width*(31.31+44*i)/85,palm_width*73/85,palm_width*2/85]) cylinder(palm_width*1.24/85,r=2.38/2,true,$fn=res);
        }
    
       //chamfer     
        translate([0,palm_width*77/85,palm_width*5/85]) rotate([360-15,0,0]) cube([palm_width,palm_width*50/85,palm_width*5/85]);

        }
    }
}

palm_cover(thumb_length, middle_length, palm_width);